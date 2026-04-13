from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.idempotency import IdempotencyKey


class IdempotencyRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, key: str) -> IdempotencyKey | None:
        res = await self.db.execute(select(IdempotencyKey).where(IdempotencyKey.key == key))
        return res.scalar_one_or_none()

    async def save(
        self,
        *,
        key: str,
        user_id: int,
        endpoint: str,
        status_code: int,
        response_body: str,
    ) -> IdempotencyKey:
        row = IdempotencyKey(
            key=key,
            user_id=user_id,
            endpoint=endpoint,
            status_code=status_code,
            response_body=response_body,
        )
        self.db.add(row)
        await self.db.flush()
        return row
