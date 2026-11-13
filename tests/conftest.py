import pytest

from app import Tea, app, database


@pytest.fixture
def filter_client(monkeypatch):
    teas = [
        Tea(
            1,
            "Jasmine Green Tea",
            "Green",
            "Floral",
            "Light green tea scented with jasmine blossoms",
            4.50,
        ),
        Tea(
            2,
            "Earl Grey",
            "Black",
            "Citrus",
            "Black tea flavored with bergamot",
            4.00,
        ),
    ]
    monkeypatch.setattr(database.catalog, "teas", teas)

    with app.test_client() as client:
        yield client


def test_type_filter_shows_only_matching_teas(filter_client):
    response = filter_client.get("/?type=Green")
    page = response.get_data(as_text=True)

    assert "Jasmine Green Tea" in page
    assert "Earl Grey" not in page


def test_profile_filter_shows_only_matching_teas(filter_client):
    response = filter_client.get("/?profile=Floral")
    page = response.get_data(as_text=True)

    assert "Jasmine Green Tea" in page
    assert "Earl Grey" not in page


def test_combined_filters_show_only_teas_matching_both(filter_client):
    response = filter_client.get("/?type=Green&profile=Floral")
    page = response.get_data(as_text=True)

    assert "Jasmine Green Tea" in page
    assert "Earl Grey" not in page


def test_no_matching_teas_shows_empty_results_message(filter_client):
    response = filter_client.get("/?type=Green&profile=Citrus")
    page = response.get_data(as_text=True)

    assert "No teas match the selected filters." in page
    assert "Jasmine Green Tea" not in page
    assert "Earl Grey" not in page


def test_main_page_shows_type_and_profile_filters(filter_client):
    response = filter_client.get("/")
    page = response.get_data(as_text=True)

    assert "Type" in page
    assert "Profile" in page
    assert "Filter" in page


# Extra inputs not named in the acceptance criteria

def test_no_filters_selected_shows_all_teas(filter_client):
    response = filter_client.get("/")
    page = response.get_data(as_text=True)

    assert "Jasmine Green Tea" in page
    assert "Earl Grey" in page


def test_unknown_type_shows_no_matching_teas(filter_client):
    response = filter_client.get("/?type=Purple")
    page = response.get_data(as_text=True)

    assert "No teas match the selected filters." in page
    assert "Jasmine Green Tea" not in page
    assert "Earl Grey" not in page


def test_unknown_profile_shows_no_matching_teas(filter_client):
    response = filter_client.get("/?profile=Smoky")
    page = response.get_data(as_text=True)

    assert "No teas match the selected filters." in page
    assert "Jasmine Green Tea" not in page
    assert "Earl Grey" not in page
