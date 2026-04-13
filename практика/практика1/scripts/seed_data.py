import asyncio
from datetime import datetime, timedelta, timezone

from sqlalchemy import text

from app.core.security import hash_password
from app.db.session import SessionLocal


async def seed() -> None:
    async with SessionLocal() as db:
        await db.execute(
            text(
                """
                INSERT INTO users (email, password_hash, role, is_active)
                VALUES
                ('admin@slotkeeper.local', :admin_hash, 'admin', true),
                ('operator@slotkeeper.local', :operator_hash, 'operator', true),
                ('viewer@slotkeeper.local', :viewer_hash, 'viewer', true)
                ON CONFLICT (email) DO NOTHING
                """
            ),
            {
                "admin_hash": hash_password("admin123"),
                "operator_hash": hash_password("operator123"),
                "viewer_hash": hash_password("viewer123"),
            },
        )

        await db.execute(
            text(
                """
                INSERT INTO warehouses (name, timezone, capacity_per_slot, is_active)
                VALUES
                ('MSK-1', 'Europe/Moscow', 20, true),
                ('SPB-1', 'Europe/Moscow', 16, true)
                ON CONFLICT (name) DO NOTHING
                """
            )
        )

        now = datetime.now(timezone.utc)
        for i in range(1, 4):
            start = now + timedelta(hours=i)
            end = start + timedelta(hours=1)
            await db.execute(
                text(
                    """
                    INSERT INTO delivery_slots (warehouse_id, start_at, end_at, capacity, reserved, version, is_deleted)
                    VALUES (1, :start_at, :end_at, 10, 0, 1, false)
                    """
                ),
                {"start_at": start, "end_at": end},
            )

        await db.execute(
            text(
                """
                INSERT INTO feature_toggles (name, enabled, rollout_percentage)
                VALUES ('carrier_integration', true, 100)
                ON CONFLICT (name) DO NOTHING
                """
            )
        )

        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed())
