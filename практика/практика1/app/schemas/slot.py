from datetime import datetime

from pydantic import BaseModel, Field


class SlotCreate(BaseModel):
    warehouse_id: int
    start_at: datetime
    end_at: datetime
    capacity: int = Field(ge=1, le=300)


class SlotUpdate(BaseModel):
    capacity: int | None = Field(default=None, ge=1, le=300)


class SlotOut(BaseModel):
    id: int
    warehouse_id: int
    start_at: datetime
    end_at: datetime
    capacity: int
    reserved: int
    version: int
    is_deleted: bool

    model_config = {"from_attributes": True}
