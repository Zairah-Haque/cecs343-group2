```mermaid
flowchart TD
    Customer -->|clicks| CartIcon["Shopping cart icon"]
    CartIcon -->|opens| System
    System -->|opens| ShippingPage["Shipping page"]
    ShippingPage -->|displays| TeasInOrder["Teas in the order"]

    Auditor -->|inspects| Database
    Auditor -->|inspects| Backup

    Customer -->|opens| MainPage["Main page"]
    MainPage -->|shows| TypeTabs["Type tabs"]
    MainPage -->|shows| ProfileFilter["Profile filter"]
    MainPage -->|shows| TeaCards["Tea cards"]
    Customer -->|clicks| TypeTabs
    TypeTabs -->|filters| TeaCards
    Customer -->|selects| ProfileFilter
    ProfileFilter -->|filters| TeaCards
    TeaCards -->|displays| Teas

    Customer -->|opens| TeasPage["/teas"]
    TeasPage -->|displays| AvailableTeas["Available teas"]
    AvailableTeas -->|"shows description and price"| Teas

    Customer -->|selects| AddButton["Add icon or button"]
    AddButton -->|adds chosen tea| Cart["Shopping cart"]

    Customer -->|views| Cart
    Cart -->|"shows name and trash can icon"| TeaInCart["Tea in cart"]
    Customer -->|selects| TrashIcon["Trash can icon"]
    TrashIcon -->|removes tea| Cart

    Customer -->|clicks repeatedly| CheckoutButton["Checkout button"]
    CheckoutButton -->|submits checkout| System
    System -->|processes without duplicates| Order
```

```mermaid
sequenceDiagram
    participant Customer
    participant MainPage
    participant TeasPage
    participant Cart
    participant System
    participant Order

    Customer->>MainPage: GET /
    MainPage-->>Customer: Tea catalog
    Customer->>MainPage: filterByType(type)
    MainPage-->>Customer: Filtered teas
    Customer->>MainPage: filterByProfile(profile)
    MainPage-->>Customer: Filtered teas
    Customer->>TeasPage: GET /teas
    TeasPage-->>Customer: Tea descriptions and prices
    Customer->>Cart: addToCart(teaId)
    Cart-->>Customer: Updated cart
    Customer->>Cart: viewCart()
    Cart-->>Customer: Cart contents
    Customer->>System: checkout(cartItems)
    System->>Order: createOrder(cartItems)
    Order-->>System: Order created
    System-->>Customer: Order confirmation
```
| UC-01 step | Action | Component that handles it |
|---|---|---|
| 1 | Customer clicks the shopping cart icon. | **Cart/navigation UI** — displays the icon and sends the customer to the shipping route when clicked. |
| 2 | System opens the shipping page. | **Shipping route in `app.py`** — handles the request and loads the shipping page template. |
| 3 | System displays the teas in the order. | **Shipping route, order/cart data, and shipping page template** — gets the teas from the customer’s order and displays them. |
