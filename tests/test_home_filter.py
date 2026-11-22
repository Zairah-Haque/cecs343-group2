"""Issue #13: browse teas by type and profile.

Unit level: Catalog.filter. Route level: GET / with the type and profile query
parameters, using the Flask test client.
"""

from app import Catalog, Tea, app, catalog

GREEN = Tea(1, "Green Tea", "Green", "Floral", "Light and fresh", 10.00)
MINT_GREEN = Tea(2, "Mint Green Tea", "Green", "Minty", "Green tea with mint", 9.00)
BLACK = Tea(3, "Black Tea", "Black", "Malty", "Full-bodied and rich", 12.00)
HERBAL = Tea(4, "Herbal Tea", "Herbal", "Minty", "Caffeine-free herbal blend", 8.00)
ALL_TEAS = [GREEN, MINT_GREEN, BLACK, HERBAL]


def _page(monkeypatch, url):
    monkeypatch.setattr(catalog, "teas", list(ALL_TEAS))
    response = app.test_client().get(url)
    assert response.status_code == 200
    return response.get_data(as_text=True)


# Unit tests: Catalog.filter


def test_filter_without_arguments_returns_every_tea():
    assert Catalog(list(ALL_TEAS)).filter(None, None) == ALL_TEAS


def test_filter_by_type_returns_only_that_type():
    assert Catalog(list(ALL_TEAS)).filter("Green", None) == [GREEN, MINT_GREEN]


def test_filter_by_profile_returns_only_that_profile():
    assert Catalog(list(ALL_TEAS)).filter(None, "Minty") == [MINT_GREEN, HERBAL]


def test_filter_by_type_and_profile_returns_only_teas_matching_both():
    assert Catalog(list(ALL_TEAS)).filter("Green", "Minty") == [MINT_GREEN]


def test_filter_with_no_match_returns_empty_list():
    assert Catalog(list(ALL_TEAS)).filter("Green", "Malty") == []


# Route tests: GET /


def test_main_page_lists_every_tea_and_both_filters(monkeypatch):
    page = _page(monkeypatch, "/")

    assert page.count("<article>") == 4
    for name in ("Green Tea", "Mint Green Tea", "Black Tea", "Herbal Tea"):
        assert name in page
    assert 'name="type"' in page
    assert 'name="profile"' in page
    for value in ("Green", "Black", "Herbal", "Floral", "Malty", "Minty"):
        assert f">{value}</option>" in page


def test_type_filter_shows_only_teas_of_that_type(monkeypatch):
    page = _page(monkeypatch, "/?type=Green")

    assert page.count("<article>") == 2
    assert "<h2>Green Tea</h2>" in page
    assert "<h2>Mint Green Tea</h2>" in page
    assert "<h2>Black Tea</h2>" not in page
    assert "<h2>Herbal Tea</h2>" not in page


def test_profile_filter_shows_only_teas_with_that_profile(monkeypatch):
    page = _page(monkeypatch, "/?profile=Malty")

    assert page.count("<article>") == 1
    assert "<h2>Black Tea</h2>" in page


def test_type_and_profile_filter_shows_only_teas_matching_both(monkeypatch):
    page = _page(monkeypatch, "/?type=Green&profile=Minty")

    assert page.count("<article>") == 1
    assert "<h2>Mint Green Tea</h2>" in page
    assert "<h2>Green Tea</h2>" not in page


def test_filter_without_match_shows_message_and_no_tea_cards(monkeypatch):
    page = _page(monkeypatch, "/?type=Green&profile=Malty")

    assert "No teas match the selected filters." in page
    assert "<article>" not in page


def test_clear_filter_link_returns_to_the_unfiltered_page(monkeypatch):
    filtered = _page(monkeypatch, "/?type=Green")
    assert 'href="/">Clear filter</a>' in filtered

    cleared = _page(monkeypatch, "/")
    assert cleared.count("<article>") == 4
