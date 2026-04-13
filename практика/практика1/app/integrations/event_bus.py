import json
import logging

from app.db.redis import redis_client

logger = logging.getLogger(__name__)


class EventBus:
    async def publish(self, topic: str, payload: dict) -> None:
        message = json.dumps(payload)
        try:
            await redis_client.publish(topic, message)
        except Exception:
            logger.warning("event_bus_publish_failed", extra={"topic": topic})
