from Student_Data import StudentsDB
import pytest

@pytest.fixture(scope='module')
def db():
    print ('---Setup---')
    db = StudentsDB()
    db.connect('../Resources/data.json')
    yield db
    print ('---TearDown---')
    db.close()

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert  scott_data['result'] == 'Pass'
    print ('Test with name {} passed'.format(scott_data['name']))

def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert  mark_data['result'] == 'Fail'
    print ('Test with name {} passed'.format(mark_data['name']))