from datetime import datetime

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import require_roles
from app.db.session import get_db
from app.models.enums import UserRole
from app.repositories.slot_repository import SlotRepository
from app.schemas.slot import SlotCreate, SlotOut
from app.services.slot_service import SlotService

router = APIRouter(prefix="/slots", tags=["slots"])


@router.post("", response_model=SlotOut, status_code=status.HTTP_201_CREATED)
async def create_slot(
    payload: SlotCreate,
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator)),
) -> SlotOut:
    service = SlotService(db, SlotRepository(db))
    slot = await service.create_slot(
        warehouse_id=payload.warehouse_id,
        start_at=payload.start_at,
        end_at=payload.end_at,
        capacity=payload.capacity,
    )
    return SlotOut.model_validate(slot)


@router.get("", response_model=list[SlotOut])
async def list_slots(
    warehouse_id: int | None = None,
    starts_after: datetime | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort_by: str = "created_at",
    sort_order: str = "desc",
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator, UserRole.viewer)),
) -> list[SlotOut]:
    service = SlotService(db, SlotRepository(db))
    rows = await service.list_slots(
        warehouse_id=warehouse_id,
        starts_after=starts_after,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return [SlotOut.model_validate(row) for row in rows]


@router.delete("/{slot_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_slot(
    slot_id: int,
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin)),
) -> None:
    service = SlotService(db, SlotRepository(db))
    await service.soft_delete_slot(slot_id)
