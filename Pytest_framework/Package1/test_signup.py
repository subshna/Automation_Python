import pytest

@pytest.yield_fixture()
def setup():
    print('Opening URL to signup')
    yield
    print('Close browser after signup')

def test_signupByEmail(setup):
    print('This is Login by email')

def test_signupByFB(setup):
    print('This is Login by FB')