import  pytest

@pytest.fixture()
def setup():
    print(" i will be executing first")
    yield
    print("i will execute later")


def test_fxture_demo(setup):
    print("i will start ")
    print("i will be executing second")



def test_fxture_demo1(setup):
    print("i will start2 ")
    print("i will be executing second2")
