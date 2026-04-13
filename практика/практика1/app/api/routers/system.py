from datetime import datetime, timezone

from fastapi import APIRouter
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.responses import Response

from app.schemas.common import HealthResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
async def healthcheck() -> HealthResponse:
    return HealthResponse(status="ok", ts=datetime.now(timezone.utc))


@router.get("/live", response_model=HealthResponse)
async def liveness() -> HealthResponse:
    return HealthResponse(status="alive", ts=datetime.now(timezone.utc))


@router.get("/ready", response_model=HealthResponse)
async def readiness() -> HealthResponse:
    # TODO: add deep checks for DB/Redis in a separate sprint.
    return HealthResponse(status="ready", ts=datetime.now(timezone.utc))


@router.get("/metrics")
async def metrics() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
