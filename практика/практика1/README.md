# SlotKeeper Service

SlotKeeper — внутренний backend-сервис управления слотами доставки и подтверждением отгрузок для B2B-маркетплейса.

## Что это за сервис

Сервис отвечает за:
- управление слотами отгрузки по складам;
- создание и сопровождение shipment-заказов;
- контроль capacity по слотам (конкурентный доступ);
- уведомление внешнего carrier API;
- аудит критичных изменений.

Типичные пользователи:
- `admin` (операционный контроль, массовые операции, управление справочниками);
- `operator` (ежедневная работа со слотами и отгрузками);
- `viewer` (read-only мониторинг).

## Быстрый старт

1. Скопировать env:
```bash
cp .env.example .env
```

2. Запустить окружение:
```bash
docker-compose up --build -d
```

3. Применить миграции:
```bash
docker-compose exec api alembic upgrade head
```

4. Засидить данные:
```bash
docker-compose exec api python scripts/seed_data.py
```

5. Открыть API:
- Swagger: http://localhost:8080/docs
- OpenAPI: http://localhost:8080/openapi.json

## Локальные команды

```bash
pip install -e .[dev]
alembic upgrade head
python scripts/seed_data.py
uvicorn app.main:app --reload --port 8080
```

## Тесты и качество

```bash
pytest -q
ruff check .
mypy app
pre-commit run --all-files
```

## Примеры API запросов

Login:
```bash
curl -X POST http://localhost:8080/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@slotkeeper.local","password":"admin123"}'
```

Создать слот:
```bash
curl -X POST http://localhost:8080/v1/slots \
  -H "Authorization: Bearer <TOKEN>" \
  -H 'Content-Type: application/json' \
  -d '{"warehouse_id":1,"start_at":"2026-04-14T10:00:00Z","end_at":"2026-04-14T11:00:00Z","capacity":10}'
```

Создать shipment c идемпотентностью:
```bash
curl -X POST http://localhost:8080/v1/shipments \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Idempotency-Key: shipment-create-EXT-1" \
  -H 'Content-Type: application/json' \
  -d '{"external_ref":"EXT-1","customer_id":"cust-1","warehouse_id":1,"slot_id":1,"total_weight_grams":1000,"address":"Moscow, Tverskaya 7","metadata_json":{}}'
```

Экспорт CSV:
```bash
curl -H "Authorization: Bearer <TOKEN>" http://localhost:8080/v1/shipments/export/csv
```

## Модель данных (кратко)

- `users`: сотрудники, роли, доступ.
- `warehouses`: справочник складов.
- `delivery_slots`: временные окна с capacity и soft delete.
- `shipments`: отгрузки клиентов.
- `audit_logs`: журнал действий.
- `idempotency_keys`: ключи идемпотентных запросов.
- `feature_toggles`: фичефлаги.

## Известные ограничения

- rate limit основан только на IP и fail-open при проблемах Redis;
- readiness endpoint пока без deep-check DB/Redis;
- legacy endpoint `/v1/legacy/free-slots` нельзя удалить из-за старых клиентов;
- частичное кеширование и местами неполная инвалидация.

Подробности: `docs/`.
