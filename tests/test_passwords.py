"""Tests for Issue #20: stored passwords cannot be read.

Unit tests check Passwords, the Database and the Backup directly. There is
no route-level test because the app has no login or sign-up route, so no
HTTP request reaches the password code.
"""

from dataclasses import fields, is_dataclass

from app import Backup, Catalog, Customer, Database, Passwords
from app import backup as app_backup
from app import database as app_database

PASSWORD = "Matcha-Latte-2026!"
DEMO_PASSWORD = "tea-shop-demo"


def readable_copies(value, password):
    """Return every place in value where the password can be read."""
    found = []

    def walk(item, path):
        if isinstance(item, str) and password in item:
            found.append(path)
        elif isinstance(item, (bytes, bytearray)) and password.encode() in item:
            found.append(path)
        elif isinstance(item, dict):
            for key, child in item.items():
                walk(key, f"{path}[key {key!r}]")
                walk(child, f"{path}[{key!r}]")
        elif isinstance(item, (list, tuple, set)):
            for index, child in enumerate(item):
                walk(child, f"{path}[{index}]")
        elif is_dataclass(item):
            for field in fields(item):
                walk(getattr(item, field.name), f"{path}.{field.name}")

    walk(value, "stored")
    if password in repr(value):
        found.append("repr()")
    return found


def database_with_customer(password):
    customer = Customer(customer_id=7, passwords=Passwords.create(password))
    return Database(catalog=Catalog(teas=[]), customers={7: customer})


def test_created_password_is_not_stored_in_readable_form():
    stored = Passwords.create(PASSWORD)

    assert readable_copies(stored, PASSWORD) == []
    assert stored.digest != PASSWORD.encode()


def test_stored_password_still_verifies_the_right_password_only():
    stored = Passwords.create(PASSWORD)

    assert stored.verify(PASSWORD) is True
    assert stored.verify("wrong-password") is False


def test_same_password_twice_gets_different_salt_and_digest():
    first = Passwords.create(PASSWORD)
    second = Passwords.create(PASSWORD)

    assert first.salt != second.salt
    assert first.digest != second.digest

def test_database_contains_no_readable_password():
    database = database_with_customer(PASSWORD)

    assert readable_copies(database, PASSWORD) == []


def test_backup_contains_no_readable_password():
    database = database_with_customer(PASSWORD)
    backup = Backup()

    backup.capture(database)

    assert 7 in backup.passwords
    assert readable_copies(backup, PASSWORD) == []


def test_backup_copy_still_verifies_the_password():
    database = database_with_customer(PASSWORD)
    backup = Backup()

    backup.capture(database)

    assert backup.passwords[7].verify(PASSWORD) is True
    assert backup.passwords[7].verify("wrong-password") is False


def test_running_app_database_and_backup_hide_the_demo_password():
    assert app_backup.passwords
    assert readable_copies(app_database, DEMO_PASSWORD) == []
    assert readable_copies(app_backup, DEMO_PASSWORD) == []
