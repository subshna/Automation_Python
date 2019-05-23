import pytest

@pytest.yield_fixture()
def setup():
    print('Opening URL to login')
    yield
    print('Close browser after login')

def test_loginByEmail(setup):
    print('This is Login by email')

def test_loginByFB(setup):
    print('This is Login by FB')