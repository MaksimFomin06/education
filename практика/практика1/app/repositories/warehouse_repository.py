from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.warehouse import Warehouse


class WarehouseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, *, name: str, timezone: str, capacity_per_slot: int) -> Warehouse:
        warehouse = Warehouse(name=name, timezone=timezone, capacity_per_slot=capacity_per_slot)
        self.db.add(warehouse)
        await self.db.flush()
        return warehouse

    async def list_all(self) -> list[Warehouse]:
        result = await self.db.execute(select(Warehouse).where(Warehouse.is_active.is_(True)))
        return list(result.scalars().all())
