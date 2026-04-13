from datetime import datetime

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    ts: datetime


class ErrorResponse(BaseModel):
    code: str
    message: str
    request_id: str | None = None
