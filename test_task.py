#!/usr/bin/env python
import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Using no parameters should invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 != t2

def test_member_access():
    """Check .field functionality of namedtuple"""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

@pytest.mark.magic
def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task('do something', 'charlie', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'charlie',
                'done': True,
                'id': 21}
    assert t_dict == expected

@pytest.mark.just_run_this
def test_replace():
    """replace() should change passed in fields"""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
