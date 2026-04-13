import json
import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError, NotFoundError
from app.db.redis import redis_client
from app.models.enums import ShipmentStatus
from app.models.shipment import Shipment
from app.repositories.audit_repository import AuditRepository
from app.repositories.idempotency_repository import IdempotencyRepository
from app.repositories.shipment_repository import ShipmentRepository
from app.services.slot_service import SlotService
from app.tasks.jobs import notify_carrier_task

logger = logging.getLogger(__name__)


class ShipmentService:
    def __init__(
        self,
        db: AsyncSession,
        shipments: ShipmentRepository,
        slots: SlotService,
        audit: AuditRepository,
        idem: IdempotencyRepository,
    ):
        self.db = db
        self.shipments = shipments
        self.slots = slots
        self.audit = audit
        self.idem = idem

    async def create_shipment(
        self,
        *,
        actor_user_id: int,
        request_id: str | None,
        idempotency_key: str | None,
        external_ref: str,
        customer_id: str,
        warehouse_id: int,
        slot_id: int | None,
        total_weight_grams: int,
        address: str,
        metadata_json: dict,
    ) -> Shipment:
        if idempotency_key:
            cached = await self.idem.get(idempotency_key)
            if cached:
                try:
                    payload = json.loads(cached.response_body)
                    shipment_id = payload.get("id")
                    if shipment_id:
                        existing = await self.shipments.get_by_id(shipment_id)
                        if existing:
                            return existing
                except Exception:
                    logger.warning("failed_to_parse_idempotent_cache")

        existing_ref = await self.shipments.get_by_external_ref(external_ref)
        if existing_ref:
            raise ConflictError("external_ref already exists")

        async with self.db.begin():
            if slot_id is not None:
                await self.slots.reserve_slot_capacity(slot_id, 1)

            shipment = Shipment(
                external_ref=external_ref,
                customer_id=customer_id,
                warehouse_id=warehouse_id,
                slot_id=slot_id,
                status=ShipmentStatus.confirmed,
                total_weight_grams=total_weight_grams,
                address=address,
                metadata_json=metadata_json,
            )
            await self.shipments.create(shipment)
            await self.audit.log(
                actor_user_id=actor_user_id,
                action="shipment_created",
                entity="shipment",
                entity_id=str(shipment.id),
                before=None,
                after={"status": shipment.status.value},
                request_id=request_id,
            )

        if idempotency_key:
            await self.idem.save(
                key=idempotency_key,
                user_id=actor_user_id,
                endpoint="POST /v1/shipments",
                status_code=201,
                response_body=json.dumps({"id": shipment.id}),
            )
            await self.db.commit()

        await redis_client.delete(f"shipments:customer:{customer_id}")
        notify_carrier_task.delay(shipment.id)
        return shipment

    async def update_status(
        self,
        *,
        shipment_id: int,
        new_status: ShipmentStatus,
        actor_user_id: int,
        request_id: str | None,
        expected_version: int | None,
    ) -> Shipment:
        shipment = await self.shipments.get_by_id(shipment_id)
        if not shipment:
            raise NotFoundError("Shipment not found")

        if expected_version is not None and expected_version != shipment.version:
            raise ConflictError("Version mismatch")

        before = {"status": shipment.status.value, "version": shipment.version}
        shipment.status = new_status
        shipment.version += 1
        await self.db.flush()
        await self.audit.log(
            actor_user_id=actor_user_id,
            action="shipment_status_updated",
            entity="shipment",
            entity_id=str(shipment.id),
            before=before,
            after={"status": shipment.status.value, "version": shipment.version},
            request_id=request_id,
        )
        await self.db.commit()
        return shipment

    async def list_shipments(
        self,
        *,
        customer_id: str | None,
        status: str | None,
        limit: int,
        offset: int,
        sort_by: str,
        sort_order: str,
    ) -> list[Shipment]:
        # Small debt: cache only for customer without status filter.
        if customer_id and not status and offset == 0:
            key = f"shipments:customer:{customer_id}"
            # Currently just a placeholder to show partial caching adoption
            _ = await redis_client.get(key)
        return await self.shipments.list(
            customer_id=customer_id,
            status=status,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
        )
