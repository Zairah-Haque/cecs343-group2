"""Unit and route-level tests for issue #14 : repeated checkout submissions."""

from types import SimpleNamespace

from app import Catalog, Database, ShoppingCart, Tea, app, customer, database


def test_repeated_order_creation_returns_one_order():
    tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
    test_customer = SimpleNamespace(
        shopping_cart=ShoppingCart(teas=[tea]),
        orders=[],
        checkout_order=None,
    )
    test_database = Database(catalog=Catalog(teas=[]))

    orders = [
        test_database.create_order(test_customer)
        for _ in range(100)
    ]

    assert all(order is orders[0] for order in orders)
    assert len(test_customer.orders) == 1
    assert len(test_database.orders) == 1
    assert test_customer.orders[0].teas == [tea]


def test_100_checkout_submissions_create_only_one_order(monkeypatch):
    tea = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)

    monkeypatch.setattr(customer, "shopping_cart", ShoppingCart(teas=[tea]))
    monkeypatch.setattr(customer, "orders", [])
    monkeypatch.setattr(customer, "checkout_order", None)
    monkeypatch.setattr(database, "orders", {})
    monkeypatch.setattr(database, "next_order_id", 1)

    client = app.test_client()
    responses = [client.post("/checkout") for _ in range(100)]

    assert all(response.status_code == 302 for response in responses)
    assert len(customer.orders) == 1
    assert len(database.orders) == 1
    assert customer.checkout_order is customer.orders[0]
    assert customer.orders[0].teas == [tea]
