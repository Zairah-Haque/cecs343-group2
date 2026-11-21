from types import SimpleNamespace

import pytest
from werkzeug.exceptions import ServiceUnavailable

from app import Tea, app, customer


@pytest.fixture
def shipping_client():
    return app.test_client()


def _order(*teas):
    return SimpleNamespace(order_id=1, shipped=False, teas=list(teas))


def test_main_path_cart_link_opens_shipping_page_with_item_quantity_and_price(
    shipping_client, monkeypatch
):
    green_tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    monkeypatch.setattr(customer, "checkout_order", _order(green_tea))

    home = shipping_client.get("/")
    response = shipping_client.get("/shipping")

    assert b'href="/shipping"' in home.data
    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "Quantity: 1" in page
    assert "$10.00" in page


def test_empty_cart_shows_the_required_message(shipping_client, monkeypatch):
    monkeypatch.setattr(customer, "checkout_order", None)
    monkeypatch.setattr(customer, "orders", [])

    response = shipping_client.get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Your cart has no items." in page
    assert "Green Tea" not in page


def test_shipping_request_503_shows_load_error(shipping_client, monkeypatch):
    class FailedShippingRequest:
        @property
        def shipped(self):
            raise ServiceUnavailable(description="We couldn’t load your order.")

    monkeypatch.setattr(customer, "checkout_order", FailedShippingRequest())

    response = shipping_client.get("/shipping")

    assert response.status_code == 503
    assert "We couldn’t load your order." in response.get_data(as_text=True)


def test_multiple_teas_in_order_are_both_displayed(shipping_client, monkeypatch):
    green_tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    earl_grey = Tea(2, "Earl Grey", "Black", "Citrus", "Bergamot", 4.00)
    monkeypatch.setattr(customer, "checkout_order", _order(green_tea, earl_grey))

    response = shipping_client.get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "Earl Grey" in page


def test_quantity_greater_than_one_is_displayed(shipping_client, monkeypatch):
    green_tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    monkeypatch.setattr(customer, "checkout_order", _order(green_tea, green_tea))

    response = shipping_client.get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Green Tea" in page
    assert "Quantity: 2" in page


def test_price_with_cents_is_displayed(shipping_client, monkeypatch):
    earl_grey = Tea(2, "Earl Grey", "Black", "Citrus", "Bergamot", 4.50)
    monkeypatch.setattr(customer, "checkout_order", _order(earl_grey))

    response = shipping_client.get("/shipping")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Earl Grey" in page
    assert "$4.50" in page
