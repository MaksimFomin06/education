from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "slotkeeper"
    app_env: Literal["local", "dev", "staging", "prod"] = "local"
    app_port: int = 8080
    log_level: str = "INFO"

    database_url: str = Field(default="postgresql+asyncpg://slotkeeper:slotkeeper@localhost:5432/slotkeeper")

    redis_url: str = "redis://localhost:6379/0"

    jwt_secret_key: str = "unsafe-local-secret"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    rate_limit_enabled: bool = True
    rate_limit_per_minute: int = 60

    enable_carrier_integration: bool = True
    enable_legacy_slot_endpoint: bool = True

    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"

    carrier_api_base_url: str = "http://localhost:8090"
    carrier_api_timeout_seconds: int = 2
    carrier_api_retries: int = 2


@lru_cache
def get_settings() -> Settings:
    return Settings()
