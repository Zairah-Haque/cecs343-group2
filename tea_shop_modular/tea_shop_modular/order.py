from dataclasses import dataclass

from .tea import Tea


@dataclass
class Order:
    order_id: int
    teas: list[Tea]
    shipped: bool = False
