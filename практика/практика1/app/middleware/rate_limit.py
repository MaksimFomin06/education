import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.config import get_settings
from app.db.redis import redis_client


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        settings = get_settings()
        if not settings.rate_limit_enabled:
            return await call_next(request)

        # Legacy behavior: limit by client host only. Behind proxies this can be unfair.
        client = request.client.host if request.client else "unknown"
        minute_bucket = int(time.time() // 60)
        key = f"rl:{client}:{minute_bucket}"

        try:
            current = await redis_client.incr(key)
            if current == 1:
                await redis_client.expire(key, 70)
        except Exception:
            # Fail-open for availability. A stricter behavior is planned for edge gateways.
            return await call_next(request)

        if current > settings.rate_limit_per_minute:
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

        return await call_next(request)
