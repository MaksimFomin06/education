from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import require_roles
from app.core.config import get_settings
from app.db.session import get_db
from app.models.enums import UserRole
from app.repositories.slot_repository import SlotRepository
from app.schemas.slot import SlotOut
from app.services.slot_service import SlotService

router = APIRouter(prefix="/legacy", tags=["legacy"])


@router.get("/free-slots", response_model=list[SlotOut])
async def legacy_free_slots(
    warehouse_id: int = Query(...),
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator, UserRole.viewer)),
) -> list[SlotOut]:
    settings = get_settings()
    if not settings.enable_legacy_slot_endpoint:
        return []

    service = SlotService(db, SlotRepository(db))
    rows = await service.list_slots(
        warehouse_id=warehouse_id,
        starts_after=None,
        limit=200,
        offset=0,
        sort_by="start_at",
        sort_order="asc",
    )
    # Legacy contract: returns slots with capacity >= reserved, even if exactly full due to old mobile clients behavior.
    return [SlotOut.model_validate(r) for r in rows if r.capacity >= r.reserved]
