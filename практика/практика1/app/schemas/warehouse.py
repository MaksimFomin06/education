from datetime import datetime

from pydantic import BaseModel


class WarehouseCreate(BaseModel):
    name: str
    timezone: str = "UTC"
    capacity_per_slot: int = 20


class WarehouseOut(BaseModel):
    id: int
    name: str
    timezone: str
    capacity_per_slot: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
