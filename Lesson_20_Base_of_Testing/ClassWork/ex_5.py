import pytest

@pytest.fixture
def my_fruit():
    return 'apple'

def test_my_fruit(my_fruit):
    assert my_fruit == 'apple'