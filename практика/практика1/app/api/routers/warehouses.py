from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import require_roles
from app.db.session import get_db
from app.models.enums import UserRole
from app.repositories.warehouse_repository import WarehouseRepository
from app.schemas.warehouse import WarehouseCreate, WarehouseOut

router = APIRouter(prefix="/warehouses", tags=["warehouses"])


@router.post("", response_model=WarehouseOut, status_code=status.HTTP_201_CREATED)
async def create_warehouse(
    payload: WarehouseCreate,
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator)),
) -> WarehouseOut:
    repo = WarehouseRepository(db)
    warehouse = await repo.create(
        name=payload.name,
        timezone=payload.timezone,
        capacity_per_slot=payload.capacity_per_slot,
    )
    await db.commit()
    return WarehouseOut.model_validate(warehouse)


@router.get("", response_model=list[WarehouseOut])
async def list_warehouses(
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator, UserRole.viewer)),
) -> list[WarehouseOut]:
    rows = await WarehouseRepository(db).list_all()
    return [WarehouseOut.model_validate(r) for r in rows]
