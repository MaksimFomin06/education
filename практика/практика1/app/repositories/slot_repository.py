from datetime import datetime

from sqlalchemy import asc, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.delivery_slot import DeliverySlot


class SlotRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, slot: DeliverySlot) -> DeliverySlot:
        self.db.add(slot)
        await self.db.flush()
        return slot

    async def get_for_update(self, slot_id: int) -> DeliverySlot | None:
        result = await self.db.execute(
            select(DeliverySlot)
            .where(DeliverySlot.id == slot_id, DeliverySlot.is_deleted.is_(False))
            .with_for_update()
        )
        return result.scalar_one_or_none()

    async def get(self, slot_id: int) -> DeliverySlot | None:
        result = await self.db.execute(
            select(DeliverySlot).where(DeliverySlot.id == slot_id, DeliverySlot.is_deleted.is_(False))
        )
        return result.scalar_one_or_none()

    async def list(
        self,
        *,
        warehouse_id: int | None,
        starts_after: datetime | None,
        limit: int,
        offset: int,
        sort_by: str,
        sort_order: str,
    ) -> list[DeliverySlot]:
        stmt = select(DeliverySlot).where(DeliverySlot.is_deleted.is_(False))
        if warehouse_id is not None:
            stmt = stmt.where(DeliverySlot.warehouse_id == warehouse_id)
        if starts_after is not None:
            stmt = stmt.where(DeliverySlot.start_at >= starts_after)

        col = DeliverySlot.created_at if sort_by not in {"start_at", "capacity", "created_at"} else getattr(DeliverySlot, sort_by)
        stmt = stmt.order_by(desc(col) if sort_order.lower() == "desc" else asc(col)).limit(limit).offset(offset)

        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def soft_delete(self, slot: DeliverySlot) -> None:
        slot.is_deleted = True
        slot.deleted_at = datetime.utcnow()  # naive dt left intentionally
        await self.db.flush()
