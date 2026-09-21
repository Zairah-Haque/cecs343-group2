from app import app


def test_customer_can_view_tea_catalog():
    response = app.test_client().get("/teas")

    assert response.status_code == 200
    assert b"Earl Grey" in response.data
