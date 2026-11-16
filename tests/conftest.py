    assert "Jasmine Green Tea" in page
    assert "$4.50" in page
    assert "No description is available." in page


def test_shipping_page_shows_two_teas_with_quantities_and_prices(monkeypatch):
    green_tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    black_tea = Tea(2, "Black Tea", "Black", "Malty", "Full-bodied and rich", 8.00)
    order = SimpleNamespace(
        order_id=1,
        shipped=False,
        teas=[green_tea, black_tea, black_tea],
    )
    monkeypatch.setattr(customer, "checkout_order", order)

    response = app.test_client().get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "Black Tea" in page
    assert "Quantity: 1" in page
    assert "Quantity: 2" in page
    assert "$10.00" in page
    assert "$8.00" in page


def test_shipping_page_shows_quantity_three(monkeypatch):
    green_tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    order = SimpleNamespace(order_id=1, shipped=False, teas=[green_tea] * 3)
    monkeypatch.setattr(customer, "checkout_order", order)

    response = app.test_client().get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "Quantity: 3" in page


def test_teas_page_displays_zero_price(monkeypatch):
    tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 0.00)
    monkeypatch.setattr(database, "get_teas", lambda: [tea])

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "$0.00" in page
