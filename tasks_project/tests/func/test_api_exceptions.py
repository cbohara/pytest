import pytest
import tasks


def test_add_raises():
    """add() should raise an expcetion with wrong type param"""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


def test_api_exceptions():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list_tasks() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate():
    """Test expected excpetions with tasks.update()"""
    def test_bad_id(self):
        """A non-int id should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                        task=tasks.Task())


    def test_bad_task(self):
        """A non-Task task should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')
