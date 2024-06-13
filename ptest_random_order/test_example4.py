import pytest

pytestmark = pytest.mark.skip(reason="Skipping all tests in this module")

def test_one():
    assert True

def test_two():
    assert True
