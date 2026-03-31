import httpx

BASE_URL = "http://127.0.0.1:8000/api/v1/products/"

def test_products_list():
    response = httpx.get(BASE_URL)

    assert response.status_code == 200

def test_create_products():
    product = {
        "name": "Book gold",
        "price": 50000,
        "quentity": 10
    }
    response = httpx.post(BASE_URL, json=product)
    assert response.status_code==201
