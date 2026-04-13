import pytest

from app.models.shipment import Shipment
from app.repositories.shipment_repository import ShipmentRepository


@pytest.mark.asyncio
async def test_create_and_get_shipment(db_session) -> None:
    repo = ShipmentRepository(db_session)
    shipment = Shipment(
        external_ref="EXT-INT-1",
        customer_id="c1",
        warehouse_id=1,
        slot_id=None,
        total_weight_grams=100,
        address="Moscow, Lenina 1",
        metadata_json={},
    )
    await repo.create(shipment)
    await db_session.commit()

    found = await repo.get_by_external_ref("EXT-INT-1")
    assert found is not None
    assert found.customer_id == "c1"
