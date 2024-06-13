# test_example.py
import pytest
import time
names="deekshay"
@pytest.mark.run(order=1)
def test_two():
    assert names=="deekshay"
    print(names)

@pytest.mark.run(order=2)
def test_one():
    assert True

def test_three():
    assert True

def test_four():
    assert True
