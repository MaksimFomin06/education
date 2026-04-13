from sqlalchemy import asc, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.shipment import Shipment


class ShipmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, shipment: Shipment) -> Shipment:
        self.db.add(shipment)
        await self.db.flush()
        return shipment

    async def get_by_id(self, shipment_id: int) -> Shipment | None:
        result = await self.db.execute(select(Shipment).where(Shipment.id == shipment_id, Shipment.is_deleted.is_(False)))
        return result.scalar_one_or_none()

    async def get_by_external_ref(self, external_ref: str) -> Shipment | None:
        result = await self.db.execute(
            select(Shipment).where(Shipment.external_ref == external_ref, Shipment.is_deleted.is_(False))
        )
        return result.scalar_one_or_none()

    async def list(
        self,
        *,
        customer_id: str | None,
        status: str | None,
        limit: int,
        offset: int,
        sort_by: str,
        sort_order: str,
    ) -> list[Shipment]:
        stmt = select(Shipment).where(Shipment.is_deleted.is_(False))
        if customer_id:
            stmt = stmt.where(Shipment.customer_id == customer_id)
        if status:
            stmt = stmt.where(Shipment.status == status)

        col = Shipment.created_at if sort_by not in {"created_at", "status", "updated_at"} else getattr(Shipment, sort_by)
        stmt = stmt.order_by(desc(col) if sort_order.lower() == "desc" else asc(col)).limit(limit).offset(offset)

        result = await self.db.execute(stmt)
        return list(result.scalars().all())
