# Tea Shop Flask starter

The classes from the class diagram are split into separate Python modules. From the parent directory, run the app with:

```bash
python -m tea_shop_modular.app
```

Install dependencies with `pip install -r tea_shop_modular/requirements.txt`. The database and backup are in memory and reset when the app stops.

## Project-file import counts

Counts include imports between Python files in this project. Flask and Python standard-library imports are excluded.

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

Files importing the top two:

- `tea.py`: `shopping_cart.py`, `order.py`, `catalog.py`, `app.py`
- `passwords.py`: `customer.py`, `backup.py`, `app.py`
