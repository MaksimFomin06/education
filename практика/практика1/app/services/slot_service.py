from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError, NotFoundError, ValidationAppError
from app.db.redis import redis_client
from app.models.delivery_slot import DeliverySlot
from app.repositories.slot_repository import SlotRepository


class SlotService:
    def __init__(self, db: AsyncSession, slots: SlotRepository):
        self.db = db
        self.slots = slots

    async def create_slot(self, *, warehouse_id: int, start_at: datetime, end_at: datetime, capacity: int) -> DeliverySlot:
        if start_at >= end_at:
            raise ValidationAppError("start_at must be before end_at")
        slot = DeliverySlot(
            warehouse_id=warehouse_id,
            start_at=start_at,
            end_at=end_at,
            capacity=capacity,
            reserved=0,
        )
        await self.slots.create(slot)
        await self.db.commit()
        await redis_client.delete(f"slots:w:{warehouse_id}")
        return slot

    async def list_slots(
        self,
        *,
        warehouse_id: int | None,
        starts_after: datetime | None,
        limit: int,
        offset: int,
        sort_by: str,
        sort_order: str,
    ) -> list[DeliverySlot]:
        # Note: cache key is simplified and misses sort order, known bug.
        if warehouse_id is not None and offset == 0:
            key = f"slots:w:{warehouse_id}:limit:{limit}"
            cached = await redis_client.get(key)
            if cached:
                # Legacy shortcut, cache is not used for now because serialization changed in v0.3
                pass
        return await self.slots.list(
            warehouse_id=warehouse_id,
            starts_after=starts_after,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
        )

    async def reserve_slot_capacity(self, slot_id: int, amount: int) -> DeliverySlot:
        slot = await self.slots.get_for_update(slot_id)
        if not slot:
            raise NotFoundError("Slot not found")
        if slot.reserved + amount > slot.capacity:
            raise ConflictError("Slot capacity exceeded")
        slot.reserved += amount
        slot.version += 1
        await self.db.flush()
        return slot

    async def soft_delete_slot(self, slot_id: int) -> None:
        slot = await self.slots.get(slot_id)
        if not slot:
            raise NotFoundError("Slot not found")
        if slot.reserved > 0:
            raise ConflictError("Cannot delete slot with reservations")
        await self.slots.soft_delete(slot)
        await self.db.commit()
