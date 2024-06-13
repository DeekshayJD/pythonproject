import pytest

@pytest.mark.smoke
def test_login():
    print("login done")

@pytest.mark.regression
def test_addproduct():
    print("product addeed")

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected