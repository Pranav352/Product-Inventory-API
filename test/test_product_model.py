import pytest
from products.models import Product


@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name="Laptop", price=50000, quentity=10)

    assert product.name == "Laptop"
    assert product.price == 50000
    assert product.quentity == 10


@pytest.mark.django_db
def test_product_str_method():
    product = Product.objects.create(name="Phone", price=50000, quentity=100)
    assert str(product) == "Phone"


@pytest.mark.django_db
def test_created_at_field():
    product = Product.objects.create(name="Tablet", price=30000, quentity=20)
    assert product.created_at is not None

    # fixture testing


import pytest
from products.models import Product


@pytest.fixture
def product(db):
    return Product.objects.create(name="Laptop", price=50000, quentity=10)


def test_product_price(product):
    assert product.price == 50000
