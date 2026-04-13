from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Header, Query, Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_request_id, require_roles
from app.db.session import get_db
from app.models.enums import UserRole
from app.models.user import User
from app.repositories.audit_repository import AuditRepository
from app.repositories.idempotency_repository import IdempotencyRepository
from app.repositories.shipment_repository import ShipmentRepository
from app.repositories.slot_repository import SlotRepository
from app.schemas.shipment import ShipmentCreate, ShipmentOut, ShipmentStatusUpdate
from app.services.export_service import ExportService
from app.services.shipment_service import ShipmentService
from app.services.slot_service import SlotService

router = APIRouter(prefix="/shipments", tags=["shipments"])


@router.post("", response_model=ShipmentOut, status_code=status.HTTP_201_CREATED)
async def create_shipment(
    payload: ShipmentCreate,
    request: Request,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_roles(UserRole.admin, UserRole.operator)),
) -> ShipmentOut:
    service = ShipmentService(
        db=db,
        shipments=ShipmentRepository(db),
        slots=SlotService(db, SlotRepository(db)),
        audit=AuditRepository(db),
        idem=IdempotencyRepository(db),
    )
    shipment = await service.create_shipment(
        actor_user_id=user.id,
        request_id=get_request_id(request),
        idempotency_key=idempotency_key,
        external_ref=payload.external_ref,
        customer_id=payload.customer_id,
        warehouse_id=payload.warehouse_id,
        slot_id=payload.slot_id,
        total_weight_grams=payload.total_weight_grams,
        address=payload.address,
        metadata_json=payload.metadata_json,
    )
    return ShipmentOut.model_validate(shipment)


@router.get("", response_model=list[ShipmentOut])
async def list_shipments(
    customer_id: str | None = None,
    status_filter: str | None = Query(default=None, alias="status"),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort_by: str = "created_at",
    sort_order: str = "desc",
    db: AsyncSession = Depends(get_db),
    _=Depends(get_current_user),
) -> list[ShipmentOut]:
    service = ShipmentService(
        db=db,
        shipments=ShipmentRepository(db),
        slots=SlotService(db, SlotRepository(db)),
        audit=AuditRepository(db),
        idem=IdempotencyRepository(db),
    )
    rows = await service.list_shipments(
        customer_id=customer_id,
        status=status_filter,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return [ShipmentOut.model_validate(row) for row in rows]


@router.patch("/{shipment_id}/status", response_model=ShipmentOut)
async def update_status(
    shipment_id: int,
    payload: ShipmentStatusUpdate,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_roles(UserRole.admin, UserRole.operator)),
) -> ShipmentOut:
    service = ShipmentService(
        db=db,
        shipments=ShipmentRepository(db),
        slots=SlotService(db, SlotRepository(db)),
        audit=AuditRepository(db),
        idem=IdempotencyRepository(db),
    )
    shipment = await service.update_status(
        shipment_id=shipment_id,
        new_status=payload.status,
        actor_user_id=user.id,
        request_id=get_request_id(request),
        expected_version=payload.expected_version,
    )
    return ShipmentOut.model_validate(shipment)


@router.get("/export/csv")
async def export_shipments_csv(
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    db: AsyncSession = Depends(get_db),
    _=Depends(require_roles(UserRole.admin, UserRole.operator)),
) -> Response:
    now = datetime.now(timezone.utc)
    date_from = date_from or now - timedelta(days=1)
    date_to = date_to or now
    csv_data = await ExportService(db).export_shipments_csv(date_from=date_from, date_to=date_to)
    return Response(content=csv_data, media_type="text/csv")


@router.post("/import/batch", status_code=status.HTTP_202_ACCEPTED)
async def import_shipments_batch(
    payload: list[ShipmentCreate],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_roles(UserRole.admin)),
) -> dict:
    service = ShipmentService(
        db=db,
        shipments=ShipmentRepository(db),
        slots=SlotService(db, SlotRepository(db)),
        audit=AuditRepository(db),
        idem=IdempotencyRepository(db),
    )
    imported = 0
    failed = 0
    for row in payload:
        try:
            await service.create_shipment(
                actor_user_id=user.id,
                request_id=None,
                idempotency_key=None,
                external_ref=row.external_ref,
                customer_id=row.customer_id,
                warehouse_id=row.warehouse_id,
                slot_id=row.slot_id,
                total_weight_grams=row.total_weight_grams,
                address=row.address,
                metadata_json=row.metadata_json,
            )
            imported += 1
        except Exception:
            failed += 1
    return {"imported": imported, "failed": failed}
