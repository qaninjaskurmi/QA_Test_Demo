==========================================================
 @public and @private -- Document your module's interface
==========================================================

This library provies two very simple decorators that document the "publicness"
of the names in your module.  They keep your module's ``__all__`` in sync so
you don't have to.

Please note that while the package is called ``public`` and it provides a
top-level module named ``public``, the PyPI package is called ``atpublic`` due
to name conflicts.


Requirements
============

``public`` requires Python 3.6 or newer.


Documentation
=============

A `simple guide`_ to using the library is available, along with a detailed
`API reference`_.


Project details
===============

 * Project home: https://gitlab.com/warsaw/public
 * Report bugs at: https://gitlab.com/warsaw/public/issues
 * Code hosting: https://gitlab.com/warsaw/public.git
 * Documentation: https://public.readthedocs.io
 * PyPI: https://pypi.python.org/pypi/atpublic

You can install it with `pip`::

    % pip install atpublic

**Do not install "public"; that is a different package!**

You can grab the latest development copy of the code using git.  The master
repository is hosted on GitLab.  If you have git installed, you can grab
your own branch of the code like this::

    $ git clone https://gitlab.com/warsaw/public.git

You may contact the author via barry@python.org.


Copyright
=========

Copyright (C) 2016-2020 Barry A. Warsaw

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Table of Contents
=================

.. toctree::
    :glob:

    docs/using
    docs/apiref
    NEWS

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _`simple guide`: docs/using.html
.. _`API reference`: docs/apiref.html
