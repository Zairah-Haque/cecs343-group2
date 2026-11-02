from dataclasses import dataclass, field

from .database import Database
from .passwords import Passwords


@dataclass
class Backup:
    passwords: dict[int, Passwords] = field(default_factory=dict)

    def capture(self, database: Database):
        self.passwords = {
            customer_id: Passwords(salt=value.passwords.salt, digest=value.passwords.digest)
            for customer_id, value in database.customers.items()
        }
