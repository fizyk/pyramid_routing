Introduction
============

**tzf.pyramid_routing** is a convenience package, that helps loading routing defined and kept in separate list.

Contents
--------

.. toctree::
   :maxdepth: 2

   install
   usage


Testing
=======

To run tests you'll need *webtest* package

- ``$ python setup.py tests``
- ``$ nosetests --cover-package=tzf.pyramid_routing --cover-tests --with-doctest --with-coverage``

Code
====

Code can be found on github: https://github.com/fizyk/pyramid_routing


TODOs
=====

- read from all lists within package (with list name becoming routes prefix)
- read routing from yml configuration
- remove trailing slash if only it is set
