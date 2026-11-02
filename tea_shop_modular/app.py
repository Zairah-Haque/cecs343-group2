from flask import Flask, redirect, render_template_string, request, url_for

from .backup import Backup
from .catalog import Catalog
from .customer import Customer
from .database import Database
from .passwords import Passwords
from .tea import Tea

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
           <a href="{{ url_for('cart_page') }}">Shopping cart</a></p>
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
    return render_template_string(
        """
        <h1>Available teas</h1><p><a href="{{ url_for('home') }}">Home</a></p>
        {% for tea in catalog.teas %}
          <article><h2>{{ tea.name }}</h2><p>{{ tea.description }}</p>
            <p>${{ '%.2f'|format(tea.price) }}</p>
            <form method="post" action="{{ url_for('add_to_cart', tea_id=tea.tea_id) }}"><button>Add to cart</button></form>
          </article>
        {% endfor %}
        """,
        catalog=catalog,
    )


@app.get("/cart")
def cart_page():
    return render_template_string(
        """
        <h1>Shopping cart</h1><p><a href="{{ url_for('home') }}">Home</a></p>
        {% for tea in customer.shopping_cart.teas %}
          <p>{{ tea.name }} — ${{ '%.2f'|format(tea.price) }}
            <form method="post" action="{{ url_for('remove_from_cart', tea_id=tea.tea_id) }}"><button>Remove</button></form>
          </p>
        {% else %}<p>Your cart is empty.</p>{% endfor %}
        <form method="post" action="{{ url_for('checkout') }}"><button>Checkout</button></form>
        """,
        customer=customer,
    )


@app.post("/cart/add/<int:tea_id>")
def add_to_cart(tea_id: int):
    tea = catalog.find(tea_id)
    if tea is not None:
        customer.shopping_cart.add(tea)
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
    return render_template_string(
        """
        <h1>Shipping page</h1><p><a href="{{ url_for('home') }}">Home</a></p>
        {% if order %}<h2>Order {{ order.order_id }}</h2>
          {% for tea in order.teas %}<p>{{ tea.name }}</p>{% endfor %}
        {% else %}<p>No unshipped order is available.</p>{% endif %}
        """,
        order=order,
    )


if __name__ == "__main__":
    app.run(debug=True)
