import builtins

from importlib import import_module

import pytest

from public import install


def test_atpublic_function(example):
    example("""\
from public import public

@public
def a_function():
    pass
""")
    module = import_module('example')
    assert module.__all__ == ['a_function']


def test_atpublic_function_runnable(example):
    example("""\
from public import public

@public
def a_function():
    return 1
""")
    module = import_module('example')
    assert module.a_function() == 1


def test_atpublic_class(example):
    example("""\
from public import public

@public
class AClass:
    pass
""")
    module = import_module('example')
    assert module.__all__ == ['AClass']


def test_atpublic_class_runnable(example):
    example("""\
from public import public

@public
class AClass:
    pass
""")
    module = import_module('example')
    assert isinstance(module.AClass(), module.AClass)


def test_atpublic_two_things(example):
    example("""\
from public import public

@public
def foo():
    pass

@public
class AClass:
    pass
""")
    module = import_module('example')
    assert module.__all__ == ['foo', 'AClass']


def test_decorator_duplicate(example):
    example("""\
from public import public

@public
def foo():
    return 1

@public
def foo():
    return 2
""")
    module = import_module('example')
    assert module.__all__ == ['foo']


def test_function_call_duplicate(example):
    example("""\
from public import public

@public
def foo():
    return 1

public(foo=2)
""")
    module = import_module('example')
    assert module.__all__ == ['foo']


def test_atpublic_append_to_all(example):
    example("""\
__all__ = ['a', 'b']

a = 1
b = 2

from public import public

@public
def foo():
    pass

@public
class AClass:
    pass
""")
    module = import_module('example')
    assert module.__all__ == ['a', 'b', 'foo', 'AClass']


def test_atpublic_keywords(example):
    example("""\
from public import public

public(a=1, b=2)
""")
    module = import_module('example')
    assert sorted(module.__all__) == ['a', 'b']


def test_atpublic_keywords_multicall(example):
    example("""\
from public import public

public(b=1)
public(a=2)
""")
    module = import_module('example')
    assert module.__all__ == ['b', 'a']


def test_atpublic_keywords_global_bindings(example):
    example("""\
from public import public

public(a=1, b=2)
""")
    module = import_module('example')
    assert module.a == 1
    assert module.b == 2


def test_atpublic_mixnmatch(example):
    example("""\
__all__ = ['a', 'b']

a = 1
b = 2

from public import public

@public
def foo():
    pass

@public
class AClass:
    pass

public(c=3)
""")
    module = import_module('example')
    assert module.__all__ == ['a', 'b', 'foo', 'AClass', 'c']


def test_all_is_a_tuple(example):
    example("""\
__all__ = ('foo',)

from public import public

def foo():
    pass

@public
def bar():
    pass
""")
    with pytest.raises(ValueError):
        import_module('example')


def test_install():
    try:
        install()
    finally:
        delattr(builtins, 'public')
