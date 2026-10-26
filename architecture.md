```mermaid
sequenceDiagram
    actor Customer
    participant MainPage as Main page
    participant TeasPage as Teas page
    participant Cart as Shopping cart
    participant System

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
    System-->>Customer: Order confirmation
```
