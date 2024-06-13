import pytest

@pytest.fixture()
def setup():
    print("start browser")
    yield
    print("close browser")

def test_1(setup):
   # print("start browser")
    print("test1 executed")
    #print("close browser")


def test_2(setup):
    #print("Test2 Executed")
    #print("start browser")
    print("test2 executed")
    #print("close browser")


def test_3(setup):
    #print("test 3 executed")
    #print("start browser")
    print("test3 executed")
    #print("close browser")
