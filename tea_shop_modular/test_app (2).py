import pytest

from tea_shop_modular import app as app_module


@pytest.fixture
def client():
    # Reset the app's in-memory data so each test starts with an empty cart.
    app_module.customer.shopping_cart.teas.clear()
    app_module.customer.orders.clear()
    app_module.customer.checkout_order = None
    app_module.database.orders.clear()
    app_module.database.next_order_id = 1

    with app_module.app.test_client() as test_client:
        yield test_client


def test_homepage_displays_tea_shop_and_a_tea(client):
    response = client.get("/")

    assert response.status_code == 201
    assert b"Tea Shop" in response.data
    assert b"Green Tea" in response.data


def test_teas_page_displays_available_teas_and_prices(client):
    response = client.get("/teas")

    assert response.status_code == 200
    assert b"Available teas" in response.data
    assert b"Green Tea" in response.data
    assert b"$10.00" in response.data


def test_customer_can_add_and_remove_a_tea_from_cart(client):
    add_response = client.post("/cart/add/1")

    assert add_response.status_code == 302
    cart_response = client.get("/cart")
    assert b"Green Tea" in cart_response.data

    remove_response = client.post("/cart/remove/1")

    assert remove_response.status_code == 302
    cart_response = client.get("/cart")
    assert b"Green Tea" not in cart_response.data


def test_checkout_creates_order_and_shows_it_on_shipping_page(client):
    client.post("/cart/add/1")

    checkout_response = client.post("/checkout")

    assert checkout_response.status_code == 302
    shipping_response = client.get("/shipping")
    assert shipping_response.status_code == 200
    assert b"Order 1" in shipping_response.data
    assert b"Green Tea" in shipping_response.data

    cart_response = client.get("/cart")
    assert b"Green Tea" not in cart_response.data
