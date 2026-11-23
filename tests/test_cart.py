"""Unit and route-level tests for Issue #10: adding tea to the cart.

Unit tests call ShoppingCart directly. Route-level tests send requests
through Flask's test client.
"""
import pytest

from app import ShoppingCart, Tea, app, catalog, customer


JASMINE = dict(
    tea_id=1,
    name="Jasmine Green Tea",
    type="Green",
    profile="Floral",
    description="Light green tea scented with jasmine blossoms",
    price=4.50,
)


@pytest.fixture
def cart_client(monkeypatch):
    """A test client with an empty cart and a one-tea menu."""
    monkeypatch.setattr(customer, "shopping_cart", ShoppingCart())
    monkeypatch.setattr(customer, "checkout_order", None)
    monkeypatch.setattr(catalog, "teas", [Tea(**JASMINE)])
    return app.test_client()


# Unit tests: test the cart without making an HTTP request.
def test_adding_a_tea_puts_it_in_the_cart():
    cart = ShoppingCart()
    tea = Tea(**JASMINE)

    cart.add(tea)

    assert cart.teas == [tea]


def test_adding_the_same_tea_twice_keeps_both_copies():
    cart = ShoppingCart()
    tea = Tea(**JASMINE)

    cart.add(tea)
    cart.add(tea)

    assert cart.teas == [tea, tea]


# Route tests: exercise adding to the cart through Flask's test client.
def test_main_path_add_to_cart_shows_tea_with_quantity_one_and_subtotal(cart_client):
    response = cart_client.post("/cart/add/1", follow_redirects=True)

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Jasmine Green Tea" in page
    assert "Quantity: 1" in page
    assert "$4.50" in page
    assert "Subtotal: $4.50" in page
    assert len(customer.shopping_cart.teas) == 1


def test_adding_the_same_tea_twice_shows_quantity_two(cart_client):
    cart_client.post("/cart/add/1")
    response = cart_client.post("/cart/add/1", follow_redirects=True)

    page = response.get_data(as_text=True)
    assert "Quantity: 2" in page
    assert "Subtotal: $9.00" in page


def test_unavailable_tea_shows_message_and_cart_stays_empty(cart_client, monkeypatch):
    monkeypatch.setattr(catalog, "teas", [Tea(**JASMINE, available_quantity=0)])

    response = cart_client.post("/cart/add/1")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Jasmine Green Tea is unavailable." in page
    assert customer.shopping_cart.teas == []


def test_cart_limit_shows_message_and_contents_stay_unchanged(cart_client):
    other_tea = Tea(2, "Earl Grey", "Black", "Citrus", "Black tea", 4.00)
    for _ in range(99):
        customer.shopping_cart.add(other_tea)

    response = cart_client.post("/cart/add/1")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "The cart limit has been reached." in page
    assert len(customer.shopping_cart.teas) == 99
    assert all(tea is other_tea for tea in customer.shopping_cart.teas)


def test_cart_service_failure_shows_message_and_cart_stays_empty(
    cart_client, monkeypatch
):
    def broken_add(tea):
        customer.shopping_cart.teas.append(tea)
        raise RuntimeError("cart service unavailable")

    monkeypatch.setattr(customer.shopping_cart, "add", broken_add)

    response = cart_client.post("/cart/add/1")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "The item could not be added." in page
    assert customer.shopping_cart.teas == []
