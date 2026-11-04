from app import Tea, app, database


def test_teas_page_shows_menu_details(monkeypatch):
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

    response = app.test_client().get("/teas")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Jasmine Green Tea" in page
    assert "Light green tea scented with jasmine blossoms" in page
    assert "$4.50" in page
    assert "Earl Grey" in page
    assert "Black tea flavored with bergamot" in page
    assert "$4.00" in page
