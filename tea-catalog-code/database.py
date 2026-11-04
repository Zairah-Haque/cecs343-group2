from dataclasses import dataclass, field

from .catalog import Catalog
from .customer import Customer
from .order import Order


@dataclass
class Database:
    catalog: Catalog
    customers: dict[int, Customer] = field(default_factory=dict)
    orders: dict[int, Order] = field(default_factory=dict)
    next_order_id: int = 1

    def get_teas(self):
        """Return the teas currently listed in the catalog."""
        return self.catalog.teas

    def create_order(self, customer):
        if customer.checkout_order is not None:
            return customer.checkout_order
        if not customer.shopping_cart.teas:
            return None

        order = Order(
            order_id=self.next_order_id,
            teas=list(customer.shopping_cart.teas),
        )
        self.next_order_id += 1
        self.orders[order.order_id] = order
        customer.orders.append(order)
        customer.shopping_cart.teas.clear()
        customer.checkout_order = order
        return order
