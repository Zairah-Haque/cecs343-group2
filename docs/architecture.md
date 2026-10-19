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
    AvailableTeas -->|shows description and price| Teas

    Customer -->|selects| AddButton["Add icon or button"]
    AddButton -->|adds chosen tea| Cart["Shopping cart"]

    Customer -->|views| Cart
    Cart -->|shows name and trash can icon| TeaInCart["Tea in cart"]
    Customer -->|selects| TrashIcon["Trash can icon"]
    TrashIcon -->|removes tea| Cart

    Customer -->|clicks repeatedly| CheckoutButton["Checkout button"]
    CheckoutButton -->|submits checkout| System
    System -->|processes without duplicates| Order
