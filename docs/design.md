```mermaid
classDiagram
    class Customer {
        +String passwords
    }
    class Order
    class Tea {
        +String type
        +String profile
        +String description
        +String price
    }
    class ShoppingCart
    class Catalog
    class Passwords
    class Database
    class Backup

    Customer -- Order
    Order -- Tea
    ShoppingCart -- Tea
    Catalog -- Tea
    Customer -- Passwords
    Database -- Passwords
    Backup -- Passwords
```
```mermaid
classDiagram
    class Tea {
        +tea_id
        +name
        +type
        +profile
        +description
        +price
    }
    class Passwords {
        +salt
        +digest
        +create(cls, password)
        +verify(self, password)
    }
    class ShoppingCart {
        +teas
        +add(self, tea)
        +remove(self, tea_id)
    }
    class Order {
        +order_id
        +teas
        +shipped
    }
    class Customer {
        +customer_id
        +passwords
        +shopping_cart
        +orders
        +checkout_order
    }
    class Catalog {
        +teas
        +filter(self, tea_type, profile)
        +find(self, tea_id)
    }
    class Database {
        +catalog
        +customers
        +orders
        +next_order_id
        +create_order(self, customer)
    }
    class Backup {
        +passwords
        +capture(self, database)
    }

    Customer "1" --> "1" Passwords : passwords
    Customer "1" --> "1" ShoppingCart : shopping_cart
    Customer "1" --> "0..*" Order : orders
    Customer "0..1" --> "1" Order : checkout_order
    ShoppingCart "1" --> "0..*" Tea : teas
    Order "1" --> "0..*" Tea : teas
    Catalog "1" --> "0..*" Tea : teas
    Database "1" --> "1" Catalog : catalog
    Database "1" --> "0..*" Customer : customers
    Database "1" --> "0..*" Order : orders
    Backup "1" --> "0..*" Passwords : passwords
    Backup ..> Database
```

| Rank | File | Project files it imports | Project files importing it |
|---:|---|---:|---:|
| 1 | `tea.py` | 0 | 4 |
| 2 | `passwords.py` | 0 | 3 |
| 3 | `order.py` | 1 | 2 |
| 4 | `catalog.py` | 1 | 2 |
| 5 | `customer.py` | 3 | 2 |
| 6 | `database.py` | 3 | 2 |
| 7 | `shopping_cart.py` | 1 | 1 |
| 8 | `backup.py` | 2 | 1 |
| 9 | `app.py` | 6 | 0 |

The top-ranked file is tea.py; four files import it: shopping_cart.py, order.py, catalog.py, and app.py. It appears as the Tea class in Prompt 2 and as tea in Prompt 1. Since the use cases mention teas, the diagrams converge on it. This is afferent coupling to tea.py.
