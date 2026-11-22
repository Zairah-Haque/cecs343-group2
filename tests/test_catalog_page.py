from types import SimpleNamespace

from app import Tea, app, customer, database, teas_page


# Unit test: call the teas view directly, without making an HTTP request.
def test_teas_page_renders_catalog_when_called_directly(monkeypatch):
    tea = Tea(
        1,
        "Jasmine Green Tea",
        "Green",
        "Floral",
        "Light green tea scented with jasmine blossoms",
        4.50,
    )
    monkeypatch.setattr(database, "get_teas", lambda: [tea])

    with app.test_request_context("/teas"):
        page = teas_page()

    assert "Jasmine Green Tea" in page
    assert "Light green tea scented with jasmine blossoms" in page
    assert "$4.50" in page


# Route tests: exercise the pages through Flask's test client.
def test_teas_page_shows_names_descriptions_and_prices(monkeypatch):
    teas = [
        Tea(
            1,
            "Jasmine Green Tea",
            "Green",
            "Floral",
            "Light green tea scented with jasmine blossoms",
            4.50,
        ),
        Tea(2, "Earl Grey", "Black", "Citrus", "Black tea flavored with bergamot", 4.00),
    ]
    monkeypatch.setattr(database, "get_teas", lambda: teas)

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Jasmine Green Tea" in page
    assert "Light green tea scented with jasmine blossoms" in page
    assert "$4.50" in page
    assert "Earl Grey" in page
    assert "Black tea flavored with bergamot" in page
    assert "$4.00" in page


def test_teas_page_shows_empty_menu_message_without_listings(monkeypatch):
    monkeypatch.setattr(database, "get_teas", lambda: [])

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "No teas are currently available." in page
    assert "<article>" not in page


def test_teas_page_shows_load_error_without_listings(monkeypatch):
    def unavailable_menu():
        raise RuntimeError("menu service unavailable")

    monkeypatch.setattr(database, "get_teas", unavailable_menu)

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "The tea menu could not be loaded." in page
    assert "<article>" not in page


def test_teas_page_shows_fallback_for_missing_description(monkeypatch):
    tea = Tea(1, "Jasmine Green Tea", "Green", "Floral", "", 4.50)
    monkeypatch.setattr(database, "get_teas", lambda: [tea])

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
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
