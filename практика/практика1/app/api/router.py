from fastapi import APIRouter

from app.api.routers import auth, legacy, shipments, slots, system, warehouses

api_router = APIRouter(prefix="/v1")
api_router.include_router(auth.router)
api_router.include_router(warehouses.router)
api_router.include_router(slots.router)
api_router.include_router(shipments.router)
api_router.include_router(legacy.router)
api_router.include_router(system.router)
