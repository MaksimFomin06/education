from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.feature_toggle import FeatureToggle


class FeatureToggleRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def is_enabled(self, name: str) -> bool:
        row = await self.db.get(FeatureToggle, name)
        return bool(row and row.enabled)

    async def get_all(self) -> list[FeatureToggle]:
        result = await self.db.execute(select(FeatureToggle))
        return list(result.scalars().all())
