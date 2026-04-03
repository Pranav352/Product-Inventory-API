import pytest

from products.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        name="Laptop",
        price=50000,
        quentity=10,
    )

    assert product.name == "Laptop"
    assert product.quentity == 10


@pytest.mark.django_db
def test_product_str_method():
    product = Product.objects.create(name="Phone", price=20000, quentity=5)

    assert str(product) == "Phone"


@pytest.mark.django_db
def test_product_quantity():
    product = Product.objects.create(name="Keyboard", price=1500, quentity=20)

    assert product.quentity > 0
