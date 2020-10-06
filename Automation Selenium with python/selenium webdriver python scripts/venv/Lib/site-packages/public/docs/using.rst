======================
 @public and @private
======================

This library provies two very simple decorators that document the "publicness"
of the names in your module.  They keep your module's ``__all__`` in sync so
you don't have to.


Background
==========

``__all__`` is great.  It has both functional and documentation purposes.

The functional purpose is that it `directly controls`_ which module names are
imported by the ``from <module> import *`` statement.  In the absence of an
``__all__``, when this statement is executed, every name in ``<module>`` that
does not start with an underscore will be imported.  This often leads to
importing too many names into the module.  That's a good enough reason not to
use ``from <module> import *`` with modules that don't have an ``__all__``.

In the presence of an ``__all__``, only the names specified in this list are
imported by the ``from <module> import *`` statement.  This in essence gives
the ``<module>`` author a way to explicitly state which names are for public
consumption.

And that's the second purpose of ``__all__``; it serves as module
documentation, explicitly naming the public objects it wants to export.  You
can print a module's ``__all__`` and get an explicit declaration of its public
API.


The problem
===========

``__all__`` has two problems.

First, it separates the declaration of a name's public export semantics from
the implementation of that name.  Usually the ``__all__`` is put at the top of
the module, although this isn't required, and in some cases it's `actively
prohibited`_.  So when you're looking at the definition of a function or class
in a module, you have to search for the ``__all__`` definition to know whether
the function or class is intended for public consumption.

This leads to the second problem, which is that it's too easy for the
``__all__`` to get `out of sync`_ with the module's contents.  Often a
function or class is renamed, removed, or added without the ``__all__`` being
updated.  Then it's difficult to know what the module author's intent was, and
it can lead to an exception when a string appearing in ``__all__`` doesn't
match an existing name in the module.  Some tools like Sphinx_ will complain
when names appear in ``__all__`` don't appear in the module.  All of this
points to the root problem; it should be easy to keep ``__all__`` in sync!


The solution
============

This package provides a way to declare a name's *publicness* right at the
point of its declaration, and to infer the name to export from that
definition.  In this way, a module's author never explicitly sets the
``__all__`` so there's no way for it to get out of sync.

This package, and Python `issue 26632`_, propose just such a solution, in the
form of a ``public`` builtin that can be used as either a decorator, or a
callable.

    >>> from public import public

You'll usually use this as a decorator, for example::

    >>> @public
    ... def foo():
    ...    pass

or::

    >>> @public
    ... class Bar:
    ...     pass

The ``__all__`` after both of those code snippets has both names in it::

    >>> print(__all__)
    ['foo', 'Bar']

Note that you do not need to initialize ``__all__`` in the module, since
``public`` will do it for you.  Of course, if your module *already* has an
``__all__``, it will add any new names to the existing list.

The requirements to use the ``@public`` decorator are simple: the decorated
thing must have a ``__name__`` attribute.  Since you'll overwhelmingly use it
to decorate functions and classes, this will always be the case.  If the
object has a ``__module__`` attribute, that string is used to look up the
module object in ``sys.modules``, otherwise the module is extracted from the
globals where the decorator is called.

There's one other common use case that isn't covered by the ``@public``
decorator.  Sometimes you want to declare simple constants or instances as
publicly available.  You can't use the ``@public`` decorator for two reasons:
constants don't have a ``__name__`` and Python's syntax doesn't allow you to
decorate such constructs.

To solve this use case, ``public`` is also a callable function accepting
keyword arguments.  An example makes this obvious::

    >>> public(SEVEN=7)
    >>> public(a_bar=Bar())

The module's ``__all__`` now contains both of the keys::

    >>> print(__all__)
    ['foo', 'Bar', 'SEVEN', 'a_bar']

and as should be obvious, the module contains name bindings for these
constants::

    >>> print(SEVEN)
    7
    >>> print(a_bar)
    <....Bar object at ...>

Multiple keyword arguments are allowed::

    >>> public(ONE=1, TWO=2)
    >>> print(__all__)
    ['foo', 'Bar', 'SEVEN', 'a_bar', 'ONE', 'TWO']

    >>> print(ONE)
    1
    >>> print(TWO)
    2


@private
========

You might also want to be explicit about your private, i.e. non-public names.
This library also provides an ``@private`` decorator for this purpose.  While
it mostly serves for documentation purposes, this decorator also ensures that
the decorated object's name does *not* appear in the ``__all__``::

    >>> from public import private

    >>> @private
    ... def foo():
    ...    pass

    >>> print(__all__)
    ['Bar', 'SEVEN', 'a_bar', 'ONE', 'TWO']

You can see here that ``foo`` has been removed from the ``__all__``.  It's
okay if the name doesn't appear in ``__all__`` at all::

    >>> @private
    ... class Baz:
    ...     pass

    >>> print(__all__)
    ['Bar', 'SEVEN', 'a_bar', 'ONE', 'TWO']

In this case, ``Baz`` never appears in ``__all__``.  Like with ``@public``,
the ``@private`` decorator will add any missing ``__all__``, but if it exists
in the module, it must be a list.  There is no functional API for ``@private``.


Making @public and @private built-ins
=====================================

It can get rather tedious if you have to add the above import in every module
where you want to use it.  What if you could put ``public`` into Python's
builtins_?  Then it would be available in all your code for free::

    >>> from public import install
    >>> install()

and now you can just use ``@public`` and ``@private`` without having to import
anything in your other modules.


Caveats
=======

There are some important usage restrictions you should be aware of:

* Only use ``@public`` and ``@private`` on top-level object.  Specifically,
  don't try to use either decorator on a class method name.  While the
  declaration won't fail, you will get an exception when you attempt to ``from
  <module> import *`` because the name pulled from ``__all__`` won't be in the
  module's globals.
* If you explicitly set ``__all__`` in your module, be sure to set it to a
  list.  Some style guides require ``__all__`` to be a tuple, but since that's
  immutable, as soon as ``@public`` tries to append to it, you will get an
  exception.  Best practice is to not set ``__all__`` explicitly; let
  ``@public`` and ``@private`` do it!
* If you still want ``__all__`` to be immutable, put the following at the
  bottom of your module::

    __all__ = tuple(__all__)


Alternatives
============

This isn't a unique approach to ``@public``.  Other_ implementations_ do
exist.  There are some subtle differences between this package and those
others.  This package:

* uses keyword arguments to map names which don't have an ``__name__``
  attribute;
* can be used to bind names and values into a module's globals;
* can optionally put ``public`` in builtins.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _`issue 26632`: http://bugs.python.org/issue26632
.. _builtins: https://docs.python.org/3/library/builtins.html
.. _`directly controls`: https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
.. _`actively prohibited`: http://pep8.readthedocs.io/en/latest/intro.html?highlight=e402#error-codes
.. _`out of sync`: http://bugs.python.org/issue23883
.. _Other: https://pypi.python.org/pypi/public
.. _implementations: http://bugs.python.org/issue22247#msg225637
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
