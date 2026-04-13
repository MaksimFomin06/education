from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.models.enums import ShipmentStatus


class ShipmentCreate(BaseModel):
    external_ref: str = Field(min_length=3, max_length=128)
    customer_id: str
    warehouse_id: int
    slot_id: int | None = None
    total_weight_grams: int = Field(ge=1)
    address: str = Field(min_length=8)
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class ShipmentStatusUpdate(BaseModel):
    status: ShipmentStatus
    expected_version: int | None = None


class ShipmentOut(BaseModel):
    id: int
    external_ref: str
    customer_id: str
    warehouse_id: int
    slot_id: int | None
    status: ShipmentStatus
    total_weight_grams: int
    address: str
    metadata_json: dict[str, Any]
    version: int
    is_deleted: bool
    created_at: datetime

    model_config = {"from_attributes": True}
