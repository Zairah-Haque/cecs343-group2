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
