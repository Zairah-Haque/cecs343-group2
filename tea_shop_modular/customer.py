from dataclasses import dataclass, field

from .order import Order
from .passwords import Passwords
from .shopping_cart import ShoppingCart


@dataclass
class Customer:
    customer_id: int
    passwords: Passwords
    shopping_cart: ShoppingCart = field(default_factory=ShoppingCart)
    orders: list[Order] = field(default_factory=list)
    checkout_order: Order | None = None
