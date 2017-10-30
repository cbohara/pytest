import pytest
import tasks
from tasks import Task


@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_demo_skip():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
def test_unique_id_demo_skipif():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def testing_unique_id(tasks_db):
    """unique_id() should return an unused id"""
    # GIVEN an initialized database
    # WHEN adding tasks to the db tasks.add returns an int
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # WHEN you request a unique object
    uid = tasks.unique_id()
    # THEN the uniqueID should be unique and not exist in ids
    assert uid not in ids

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demostrate xfail"""
    uid = tasks.unique_id()
    assert uid == 'a duck'

@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demostrate xpass"""
    uid = tasks.unique_id()
    assert uid != 'a duck'
