# Incident Notes

## INC-2026-02-17: Slot overbooking spike

- Симптом: редкие overbooking при всплеске запросов.
- Причина: старый код резервирования без row-level lock.
- Что сделали: перевели create shipment на `SELECT FOR UPDATE`.
- Остаточный риск: legacy path всё ещё может обойти новый сервисный метод.

## INC-2026-03-29: Carrier API timeout cascade

- Симптом: рост latency у create shipment из-за sync-вызовов интеграции.
- Причина: вызов carrier из request path.
- Что сделали: отправку вынесли в Celery retry task.
- Остаточный риск: нет circuit-breaker, только retry.
