import mathLib
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (2,7), reason="Skipped as version")
def test_calc_add():
    assert mathLib.add(10, 20) == 30
    print (mathLib.add(10, 20), '------')
    assert mathLib.sub(10, 20) == -10
    assert mathLib.mul(10, 20) == 200
    assert mathLib.div(20, 10) == 2

def test_add_string():
    res = mathLib.add('Hello', ' World')
    assert res == 'Hello World'
    assert type(res) is str
    assert 'Hello' in res