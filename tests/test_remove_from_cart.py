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
def remove_cart_client(monkeypatch):
    """A test client with an empty cart and a one-tea menu."""
    monkeypatch.setattr(customer, "shopping_cart", ShoppingCart())
    monkeypatch.setattr(customer, "checkout_order", None)
    monkeypatch.setattr(catalog, "teas", [Tea(**JASMINE)])
    return app.test_client()


# Unit test: test cart behavior without making an HTTP request.
def test_removing_a_tea_removes_one_matching_copy():
    cart = ShoppingCart()
    tea = Tea(**JASMINE)
    cart.add(tea)
    cart.add(tea)

    cart.remove(tea.tea_id)

    assert cart.teas == [tea]


# Route tests: exercise cart behavior through Flask's test client.
def test_main_path_remove_tea_from_cart(remove_cart_client):
    customer.shopping_cart.add(Tea(**JASMINE))

    response = remove_cart_client.post(
        "/cart/remove/1",
        follow_redirects=True,
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Jasmine Green Tea" not in page
    assert customer.shopping_cart.teas == []


def test_removing_one_tea_keeps_other_teas_in_the_cart(remove_cart_client):
    jasmine = Tea(**JASMINE)
    earl_grey = Tea(
        2,
        "Earl Grey",
        "Black",
        "Citrus",
        "Black tea flavored with bergamot",
        4.00,
    )
    customer.shopping_cart.add(jasmine)
    customer.shopping_cart.add(earl_grey)

    response = remove_cart_client.post(
        "/cart/remove/1",
        follow_redirects=True,
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Jasmine Green Tea" not in page
    assert "Earl Grey" in page
    assert customer.shopping_cart.teas == [earl_grey]


def test_removing_the_last_tea_shows_empty_cart_message(remove_cart_client):
    customer.shopping_cart.add(Tea(**JASMINE))

    response = remove_cart_client.post(
        "/cart/remove/1",
        follow_redirects=True,
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Your cart is empty." in page
    assert "Jasmine Green Tea" not in page


def test_trash_icon_removes_the_selected_tea(remove_cart_client):
    jasmine = Tea(**JASMINE)
    earl_grey = Tea(
        2,
        "Earl Grey",
        "Black",
        "Citrus",
        "Black tea flavored with bergamot",
        4.00,
    )
    chamomile = Tea(
        3,
        "Chamomile",
        "Herbal",
        "Floral",
        "A light herbal tea",
        3.50,
    )
    customer.shopping_cart.add(jasmine)
    customer.shopping_cart.add(earl_grey)
    customer.shopping_cart.add(chamomile)

    response = remove_cart_client.post(
        "/cart/remove/2",
        follow_redirects=True,
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Earl Grey" not in page
    assert "Jasmine Green Tea" in page
    assert "Chamomile" in page
    assert customer.shopping_cart.teas == [jasmine, chamomile]


def test_removing_a_tea_reduces_its_quantity_by_one(remove_cart_client):
    remove_cart_client.post("/cart/add/1")
    remove_cart_client.post("/cart/add/1")

    response = remove_cart_client.post(
        "/cart/remove/1",
        follow_redirects=True,
    )
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Jasmine Green Tea" in page
    assert "Quantity: 1" in page
    assert "Subtotal: $4.50" in page
    assert customer.shopping_cart.teas == [catalog.teas[0]]


def test_empty_cart_shows_empty_cart_message(remove_cart_client):
    response = remove_cart_client.get("/cart")
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Your cart is empty." in page
    assert "Jasmine Green Tea" not in page
