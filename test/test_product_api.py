import httpx

BASE_URL = "http://127.0.0.1:8000/api/v1/products/"

# def test_create_product():
#     product_data = {
#         "name": "Equipment",
#         "price": 500000,
#         "quentity": 10
#     }

#     response = httpx.post(BASE_URL, json=product_data)

# assert response.status_code == 201


def test_get_products():
    response = httpx.get(BASE_URL)

    assert response.status_code == 200
    # assert isinstance(response.json(), list)


def test_get_single_product():
    response = httpx.get(BASE_URL + "/1")

    assert response.status_code in [200, 404]


def test_update_product():
    update_data = {"name": "Equipment", "price": 55000, "quentity": 15}

    response = httpx.put(BASE_URL + "31/", json=update_data)

    assert response.status_code in [200, 404]


def test_delete_product():
    response = httpx.delete(BASE_URL + "25/")
    assert response.status_code in [204, 404]
