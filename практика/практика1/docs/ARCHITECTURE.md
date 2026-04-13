# Architecture Overview

## Layers

- `app/api`: REST endpoints, deps, request/response orchestration.
- `app/services`: бизнес-правила, транзакции, orchestration.
- `app/repositories`: SQLAlchemy data access.
- `app/models`: ORM-сущности.
- `app/tasks`: фоновые задачи Celery.
- `app/integrations`: внешние клиенты.
- `app/core`: конфиг, безопасность, ошибки, логирование.
- `app/middleware`: request-id, rate limiting.

## Main flow: create shipment

1. Auth + RBAC (`operator`/`admin`).
2. Проверка идемпотентности.
3. Транзакция:
- lock слота `SELECT ... FOR UPDATE`;
- резерв capacity;
- вставка shipment;
- audit log.
4. Сброс cache key.
5. Async notify в carrier через Celery.

## Why this is realistic

- есть legacy endpoint;
- есть компромиссные решения и TODO;
- не все участки одинаково чистые;
- виден переход от старого к новому подходу.
