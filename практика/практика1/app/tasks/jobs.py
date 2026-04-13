import asyncio
import logging

from sqlalchemy import select

from app.db.session import SessionLocal
from app.integrations.carrier_client import CarrierClient
from app.models.shipment import Shipment
from app.tasks.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def notify_carrier_task(self, shipment_id: int) -> None:  # noqa: ANN001
    asyncio.run(_notify_carrier_async(shipment_id))


async def _notify_carrier_async(shipment_id: int) -> None:
    async with SessionLocal() as db:
        result = await db.execute(select(Shipment).where(Shipment.id == shipment_id))
        shipment = result.scalar_one_or_none()
        if not shipment:
            logger.warning("notify_carrier_shipment_not_found", extra={"shipment_id": shipment_id})
            return

        client = CarrierClient()
        payload = {
            "shipment_id": shipment.id,
            "external_ref": shipment.external_ref,
            "address": shipment.address,
            "status": shipment.status.value,
        }
        response = await client.notify_shipment(payload)
        logger.info("carrier_notified", extra={"shipment_id": shipment_id, "carrier_response": response})
