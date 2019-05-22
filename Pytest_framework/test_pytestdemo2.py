import pytest

@pytest.yield_fixture() # scope='module' to execute once all method
def setup():
    print ('Once before every method')
    yield
    print ('Once After every method')

def test_method1(setup):
    print('Test method1')

def test_method2(setup):
    print('Test method2')