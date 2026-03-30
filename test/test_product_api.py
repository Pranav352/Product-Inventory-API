import httpx

BASE_URL = "http://127.0.0.1:8000/api/v1/products/"


def test_get_products():
    response = httpx.get(BASE_URL)

    assert response.status_code == 200


# Insert product test
# import httpx

# def test_create_product():

#     data = {
#         "name": "Laptop",
#         "price": 50000,
#         "quentity": 10
#     }

#     response = httpx.post(
#         "http://127.0.0.1:8000/api/v1/products/",
#         json=data
#     )

#     assert response.status_code == 201


# # delete test
# import httpx

# def test_delete_product():

#     response = httpx.delete(
#         "http://127.0.0.1:8000/api/v1/products/13/"
#     )

#     assert response.status_code in [200, 204]


# client assertation
# import httpx

# BASE_URL = "http://127.0.0.1:8000"

# def test_products():

#     with httpx.Client(base_url=BASE_URL) as client:

#         response = client.get("/api/v1/products/")

#         assert response.status_code == 200
