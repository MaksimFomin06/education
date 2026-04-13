# Known Tech Debt

1. Некорректный cache key в `SlotService.list_slots` (sort_order не учитывается).
2. `deleted_at` в `SlotRepository.soft_delete` пишется как naive datetime.
3. `import/batch` делает N последовательных транзакций без bulk/queue.
4. Readiness endpoint не проверяет DB/Redis.
5. Rate limit по `request.client.host` плохо работает за NAT/proxy.
6. Есть дублирование инициализации сервисов в роутерах.
7. Нет cleanup job для `idempotency_keys`.
8. Coverage по негативным сценариям явно недостаточное.
