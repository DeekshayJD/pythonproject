import  pytest

@pytest.fixture()
def setup():
    print(" i will be executing first")


def test_fxture_demo(setup):
    print("i will be executing second")

