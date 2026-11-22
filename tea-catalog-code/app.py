from __future__ import annotations

import hashlib
import hmac
import secrets
from dataclasses import dataclass, field

from flask import Flask, redirect, render_template_string, request, url_for


@dataclass
class Tea:
    tea_id: int
    name: str
    type: str
    profile: str
    description: str
    price: float
    available_quantity: int | None = None


@dataclass
class Passwords:
    salt: bytes
    digest: bytes

    @classmethod
    def create(cls, password):
        salt = secrets.token_bytes(16)
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
        return cls(salt=salt, digest=digest)

    def verify(self, password):
        candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), self.salt, 200_000)
        return hmac.compare_digest(candidate, self.digest)


@dataclass
class ShoppingCart:
    teas: list[Tea] = field(default_factory=list)

    def add(self, tea):
        self.teas.append(tea)

    def remove(self, tea_id):
        for index, tea in enumerate(self.teas):
            if tea.tea_id == tea_id:
                del self.teas[index]
                return


@dataclass
class Order:
    order_id: int
    teas: list[Tea]
    shipped: bool = False


@dataclass
class Customer:
    customer_id: int
    passwords: Passwords
    shopping_cart: ShoppingCart = field(default_factory=ShoppingCart)
    orders: list[Order] = field(default_factory=list)
    checkout_order: Order | None = None


@dataclass
class Catalog:
    teas: list[Tea]

    def filter(self, tea_type, profile):
        return [
            tea
            for tea in self.teas
            if (tea_type is None or tea.type == tea_type)
            and (profile is None or tea.profile == profile)
        ]

    def find(self, tea_id):
        return next((tea for tea in self.teas if tea.tea_id == tea_id), None)


@dataclass
class Database:
    catalog: Catalog
    customers: dict[int, Customer] = field(default_factory=dict)
    orders: dict[int, Order] = field(default_factory=dict)
    next_order_id: int = 1

    def get_teas(self):
        """Return the teas currently listed in the catalog."""
        return self.catalog.teas

    def create_order(self, customer):
        if customer.checkout_order is not None:
            return customer.checkout_order
        if not customer.shopping_cart.teas:
            return None

        order = Order(
            order_id=self.next_order_id,
            teas=list(customer.shopping_cart.teas),
        )
        self.next_order_id += 1
        self.orders[order.order_id] = order
        customer.orders.append(order)
        customer.shopping_cart.teas.clear()
        customer.checkout_order = order
        return order


@dataclass
class Backup:
    passwords: dict[int, Passwords] = field(default_factory=dict)

    def capture(self, database):
        self.passwords = {
            customer_id: Passwords(salt=value.passwords.salt, digest=value.passwords.digest)
            for customer_id, value in database.customers.items()
        }


teas = [
    Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00),
    Tea(2, "Black Tea", "Black", "Malty", "Full-bodied and rich", 12.00),
    Tea(3, "Herbal Tea", "Herbal", "Minty", "Caffeine-free herbal blend", 8.00),
]
catalog = Catalog(teas=teas)
customer = Customer(customer_id=1, passwords=Passwords.create("tea-shop-demo"))
database = Database(catalog=catalog, customers={customer.customer_id: customer})
backup = Backup()
backup.capture(database)

app = Flask(__name__)


@app.get("/")
def home():
    tea_type = request.args.get("type") or None
    profile = request.args.get("profile") or None
    shown_teas = catalog.filter(tea_type=tea_type, profile=profile)
    tea_types = sorted({tea.type for tea in catalog.teas})
    profiles = sorted({tea.profile for tea in catalog.teas})
    return render_template_string(
        """
        <h1>Tea Shop</h1>
        <p><a href="{{ url_for('teas_page') }}">All teas</a> ·
           <a href="{{ url_for('shipping_page') }}" aria-label="Shopping cart">🛒 Shopping cart</a></p>
        <form method="get">
          <label>Type <select name="type"><option value="">All</option>
            {% for value in tea_types %}<option {% if value == tea_type %}selected{% endif %}>{{ value }}</option>{% endfor %}
          </select></label>
          <label>Profile <select name="profile"><option value="">All</option>
            {% for value in profiles %}<option {% if value == profile %}selected{% endif %}>{{ value }}</option>{% endfor %}
          </select></label>
          <button>Filter</button>
          <a href="{{ url_for('home') }}">Clear filter</a>
        </form>
        {% if not shown_teas %}<p>No teas match the selected filters.</p>{% endif %}
        {% for tea in shown_teas %}
          <article><h2>{{ tea.name }}</h2><p>{{ tea.description }} · ${{ '%.2f'|format(tea.price) }}</p>
            <form method="post" action="{{ url_for('add_to_cart', tea_id=tea.tea_id) }}"><button>Add to cart</button></form>
          </article>
        {% endfor %}
        """,
        shown_teas=shown_teas,
        tea_types=tea_types,
        profiles=profiles,
        tea_type=tea_type,
        profile=profile,
    )


@app.get("/teas")
def teas_page():
    try:
        available_teas = database.get_teas()
    except Exception:
        available_teas = None

    return render_template_string(
        """
        <h1>Available teas</h1><p><a href="{{ url_for('home') }}">Home</a></p>
        {% if available_teas is none %}
          <p>The tea menu could not be loaded.</p>
        {% elif not available_teas %}
          <p>No teas are currently available.</p>
        {% else %}
          {% for tea in available_teas %}
            <article><h2>{{ tea.name }}</h2>
              <p>{% if tea.description %}{{ tea.description }}{% else %}No description is available.{% endif %}</p>
              <p>${{ '%.2f'|format(tea.price) }}</p>
            </article>
          {% endfor %}
        {% endif %}
        """,
        available_teas=available_teas,
    )


def _render_cart(message=None):
    items_by_id = {}

    for tea in customer.shopping_cart.teas:
        if tea.tea_id in items_by_id:
            items_by_id[tea.tea_id]["quantity"] += 1
        else:
            items_by_id[tea.tea_id] = {"tea": tea, "quantity": 1}

    items = list(items_by_id.values())
    subtotal = sum(
        item["tea"].price * item["quantity"]
        for item in items
    )

    return render_template_string(
        """
        <h1>Shopping cart</h1>
        <p><a href="{{ url_for('home') }}">Home</a></p>

        {% if message %}
          <p role="alert">{{ message }}</p>
        {% endif %}

        {% if items %}
          <ul>
            {% for item in items %}
              <li>
                <span>{{ item.tea.name }}</span>
                <form
                  method="post"
                  action="{{ url_for('remove_from_cart', tea_id=item.tea.tea_id) }}"
                  style="display: inline"
                >
                  <button
                    type="submit"
                    aria-label="Remove one {{ item.tea.name }} from cart"
                    title="Remove one {{ item.tea.name }} from cart"
                  >🗑</button>
                </form>
                — Quantity: {{ item.quantity }}
                — ${{ '%.2f'|format(item.tea.price) }} each
              </li>
            {% endfor %}
          </ul>
        {% else %}
          <p>Your cart is empty.</p>
        {% endif %}

        <p>Subtotal: ${{ '%.2f'|format(subtotal) }}</p>

        <form method="post" action="{{ url_for('checkout') }}">
          <button type="submit">Checkout</button>
        </form>
        """,
        items=items,
        subtotal=subtotal,
        message=message,
    )

@app.get("/cart")
def cart_page():
    return _render_cart()


@app.post("/cart/add/<int:tea_id>")
def add_to_cart(tea_id: int):
    tea = catalog.find(tea_id)
    if tea is None:
        return _render_cart("That tea is unavailable.")
    if getattr(tea, "available_quantity", None) == 0:
        return _render_cart(f"{tea.name} is unavailable.")
    if len(customer.shopping_cart.teas) >= 99:
        return _render_cart("The cart limit has been reached.")

    previous_items = list(customer.shopping_cart.teas)
    try:
        customer.shopping_cart.add(tea)
    except Exception:
        customer.shopping_cart.teas[:] = previous_items
        return _render_cart("The item could not be added.")

    customer.checkout_order = None
    return redirect(url_for("cart_page"))


@app.post("/cart/remove/<int:tea_id>")
def remove_from_cart(tea_id: int):
    customer.shopping_cart.remove(tea_id)
    return redirect(url_for("cart_page"))


@app.post("/checkout")
def checkout():
    database.create_order(customer)
    return redirect(url_for("shipping_page"))


@app.get("/shipping")
def shipping_page():
    order = customer.checkout_order
    if order is None or order.shipped:
        order = next((item for item in reversed(customer.orders) if not item.shipped), None)

    teas_to_show = order.teas if order is not None else customer.shopping_cart.teas
    items_by_id = {}
    for tea in teas_to_show:
        if tea.tea_id in items_by_id:
            items_by_id[tea.tea_id]["quantity"] += 1
        else:
            items_by_id[tea.tea_id] = {"tea": tea, "quantity": 1}

    return render_template_string(
        """
        <h1>Shipping page</h1><p><a href="{{ url_for('home') }}">Home</a></p>
        {% if order %}<h2>Order {{ order.order_id }}</h2>
        {% endif %}
        {% if items %}
          {% for item in items %}
            <p>{{ item.tea.name }} — Quantity: {{ item.quantity }} — ${{ '%.2f'|format(item.tea.price) }}</p>
          {% endfor %}
        {% else %}<p>Your cart has no items.</p>{% endif %}
        """,
        order=order,
        items=list(items_by_id.values()),
    )


@app.errorhandler(503)
def shipping_unavailable(error):
    return render_template_string(
        "<h1>Shipping page</h1><p>We couldn’t load your order.</p>"
    ), 503


if __name__ == "__main__":
    app.run(debug=True)


