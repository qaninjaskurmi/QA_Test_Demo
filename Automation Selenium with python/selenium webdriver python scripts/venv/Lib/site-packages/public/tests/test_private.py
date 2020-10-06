from importlib import import_module

import pytest


def test_atprivate(example):
    example("""\
from public import private

@private
def a_function():
    pass
""")
    module = import_module('example')
    assert 'a_function' not in module.__all__


def test_atprivate_with_dunder_all(example):
    example("""\
from public import private

__all__ = ['a_function']

@private
def a_function():
    pass
""")
    module = import_module('example')
    assert 'a_function' not in module.__all__


def test_atprivate_adds_dunder_all(example):
    example("""\
from public import private

@private
def a_function():
    pass
""")
    module = import_module('example')
    assert module.__all__ == []


def test_all_is_a_tuple(example):
    example("""\
__all__ = ('foo',)

from public import private

def foo():
    pass

@private
def bar():
    pass
""")
    with pytest.raises(ValueError):
        import_module('example')
