from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_log import AuditLog


class AuditRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log(
        self,
        *,
        actor_user_id: int | None,
        action: str,
        entity: str,
        entity_id: str,
        before: dict | None,
        after: dict | None,
        request_id: str | None,
    ) -> None:
        record = AuditLog(
            actor_user_id=actor_user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
            before=before,
            after=after,
            request_id=request_id,
        )
        self.db.add(record)
        await self.db.flush()
