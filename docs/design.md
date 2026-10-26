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
