def test_unauthorized_shipments_list(client) -> None:
    response = client.get("/v1/shipments")
    assert response.status_code == 401
