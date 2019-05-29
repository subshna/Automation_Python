import mathLib
import pytest

@pytest.mark.parametrize('num1, num2, result',
                          [
                              (7, 3, 10),
                              ('Hello', ' World', 'Hello World'),
                              (10.5, 20.3, 30.8)
                          ])
def test_add(num1, num2, result):
    assert mathLib.add(num1, num2) == result