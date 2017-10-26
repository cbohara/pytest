"""Test the tasks.add() API function"""
import pytest
import tasks
from tasks import Task

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing and disconnect after"""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

def equivalent(t1, t2):
    """Check 2 tasks for equivalence"""
    # compare everything but the id field
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))

def test_add():
    """tasks.get() using id returned from add() works"""
    task = Task('breath', 'Charlie', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should be the same
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                         Task('wake', 'brian'),
                         Task('breath', 'Brian', True),
                         Task('exercise', 'BrIAn', False)])
def test_add_many_alt1(task):
    """Demonstrate parameterize"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('summary, owner, done',
                        [('sleep', None, False),
                        ('wake', 'brian', False),
                        ('breath', 'BRIAN', True),
                        ('eat eggs', 'BriAN', False),
                        ])
def test_add_many_alt2(summary, owner, done):
    """Demonstrate parameterize"""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BriAn', False))

@pytest.mark.parametrize('task', tasks_to_try)
def test_add_many_alt3(task):
    """I like this one but the output is not very helpful"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]
print tasks_to_try
print task_ids

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_many_alt4(task):
    """Alt to get better pytest output"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_many_alt5(task):
    """Demo pytest.param and id"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
