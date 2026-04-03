import pytest

from products.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    data = {
        "name": "Test",
        "price": 55000,
        "quentity": 15,
    }
    Serializer = ProductSerializer(data=data)
    assert Serializer.is_valid()


@pytest.mark.django_db
def test_product_serializers_invalid():
    data = {
        "name": "",
        "price": 55000,
        "quentity": 15,
    }
    serializer = ProductSerializer(data=data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_product_serializers_output():
    data = {
        "name": "Test",
        "price": 55000,
        "quentity": 15,
    }
    serializer = ProductSerializer(data=data)
    serializer.is_valid()
    assert data["name"] == "Test"
    assert data["price"] == 55000
