# Changelog

## 0.5.0 - 2026-04-13
- Добавлен endpoint `POST /v1/shipments/import/batch`.
- Переведены carrier notifications в Celery retries.
- Добавлены feature_toggles таблица и fallback behavior.
- Включён request-id middleware и JSON structured logging.

## 0.4.2 - 2026-03-28
- Исправлен deadlock в старом процессе выделения слотов (частично).
- Добавлен legacy endpoint `/v1/legacy/free-slots` для backward compatibility.

## 0.4.0 - 2026-03-11
- Миграция на SQLAlchemy 2 async начата, но не завершена.
- Обновлён формат audit events.
