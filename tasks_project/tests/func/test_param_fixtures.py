import pytest
import tasks
from tasks import Task


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'charlie'),
                Task('breath', 'cHArlie'),
                Task('exercise', 'CHARLIE', True))


def id_func(fixture_value):
    """A function for generating ids"""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)


# customize the string used in a test ID by using ids keyword arg
@pytest.fixture(params=tasks_to_try, ids=id_func)
def request_task(request):
    """Using id_func to generate ids"""
    print '\n' + str(request.param)
    return request.param


def equivalent(t1, t2):
    """Check two tasks are equivalent"""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


def test_add(tasks_db, request_task):
    """Use fixture with generated ids"""
    task_id = tasks.add(request_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, request_task)
