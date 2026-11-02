from dataclasses import dataclass


@dataclass
class Tea:
    tea_id: int
    name: str
    type: str
    profile: str
    description: str
    price: float
