import pytest
from rest_framework.test import APIClient
from products.models import Product


@pytest.mark.django_db
def test_get_products():

    Product.objects.create(name="Laptop", price=50000, quentity=10)

    client = APIClient()
    response = client.get("/api/v1/Product/")
