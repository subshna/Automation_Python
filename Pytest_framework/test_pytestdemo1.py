import pytest

@pytest.fixture()
def setup():
    print('Once before every method')

def test_method1(setup):
    print('Test method1')

def test_method2(setup):
    print('Test method2')