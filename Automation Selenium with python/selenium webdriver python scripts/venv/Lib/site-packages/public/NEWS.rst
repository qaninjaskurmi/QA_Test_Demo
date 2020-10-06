==============
 @public NEWS
==============

2.0 (2020-07-27)
================
* Drop Python 3.4 and 3.5; add Python 3.8 and 3.9.
* The C implementation is removed. (GL#4)
* Added an ``@private`` decorator (GL#3)
* Build and test on Windows in addition to Linux.
* Fix the doctests so that they actually run and pass!
* Add type annotations and API reference documentation.
* Internal improvements and modernizations.

1.0 (2017-09-15)
================
* 1.0 release.
* Documentation improvements.

0.5 (2016-12-14)
================
* Fix MANIFEST.in inclusion of the src directory for the C extension.

0.4 (2016-11-28)
================
* Add Python 3.6 support.
* Make building the C extension optional, for environments without a C
  compiler.

0.3 (2016-05-25)
================
* Raise ``ValueError`` when ``__all__`` isn't a list (or subclass) instance.

0.2 (2016-05-22)
================
* Documentation updates based on initial feedback.
* Some minor test suite clean up.

0.1 (2016-05-09)
================
* Initial release.
