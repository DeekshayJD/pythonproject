import pytest

@pytest.mark.smoke
def test_login():
    print("login done")

@pytest.mark.regression
def test_addproduct():
    print("product addeed")

