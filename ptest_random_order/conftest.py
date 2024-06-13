# conftest.py
import time
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    # Add a delay of 2 seconds between each test
    time.sleep(2)
