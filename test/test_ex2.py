import pytest


@pytest.fixture
def yield_fixture():
    print("start case ")
    yield 6
    print("end case ")


def test_example1(yield_fixture):
    print("run-example-1 ")
    assert yield_fixture == 6
