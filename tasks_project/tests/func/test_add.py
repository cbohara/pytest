import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer"""
    # GIVEN an initialized db
    # WHEN a new task is added
    new_task = Task('do something')
    # THEN returned task_id is of type int
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affects task.count()"""
    # GIVEN an initialized db with 3 tasks
    # WHEN another task is added
    tasks.add(Task('do something'))
    # THEN the count increases by one
    assert tasks.count() == 4
