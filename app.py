from flask import Flask, render_template_string

app = Flask(__name__)

TEAS = [
    {"name": "Earl Grey", "description": "Black tea with bergamot", "price": 8.00},
    {"name": "Jasmine Green", "description": "Green tea with jasmine", "price": 9.50},
]

CATALOG_TEMPLATE = """
<!doctype html>
<title>Tea Shop</title>
<h1>Tea Shop</h1>
<ul>
  {% for tea in teas %}
    <li>
      <strong>{{ tea.name }}</strong> — {{ tea.description }} — ${{ "%.2f"|format(tea.price) }}
    </li>
  {% endfor %}
</ul>
"""


@app.get("/teas")
def tea_catalog():
    return render_template_string(CATALOG_TEMPLATE, teas=TEAS)


if __name__ == "__main__":
    app.run(debug=True)
