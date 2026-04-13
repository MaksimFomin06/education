from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.shipment import Shipment


class ExportService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def export_shipments_csv(self, *, date_from: datetime, date_to: datetime) -> str:
        result = await self.db.execute(
            select(Shipment).where(Shipment.created_at >= date_from, Shipment.created_at <= date_to)
        )
        rows = result.scalars().all()
        lines = ["id,external_ref,customer_id,status,created_at"]
        for row in rows:
            lines.append(f"{row.id},{row.external_ref},{row.customer_id},{row.status.value},{row.created_at.isoformat()}")
        return "\n".join(lines)
