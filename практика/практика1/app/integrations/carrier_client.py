import asyncio
import logging
from typing import Any

import httpx

from app.core.config import get_settings

logger = logging.getLogger(__name__)


class CarrierClient:
    def __init__(self) -> None:
        settings = get_settings()
        self.base_url = settings.carrier_api_base_url
        self.timeout = settings.carrier_api_timeout_seconds
        self.retries = settings.carrier_api_retries

    async def notify_shipment(self, payload: dict[str, Any]) -> dict[str, Any]:
        last_exc: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                async with httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout) as client:
                    response = await client.post("/carrier/shipments", json=payload)
                    response.raise_for_status()
                    return response.json()
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
                logger.warning("carrier_notify_failed", extra={"attempt": attempt + 1, "error": str(exc)})
                await asyncio.sleep(0.2 * (attempt + 1))
        raise RuntimeError(f"carrier integration failed: {last_exc}")
