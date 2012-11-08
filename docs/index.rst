.. tzf.pyramid_routing documentation master file, created by
   sphinx-quickstart on Thu Nov  8 20:47:06 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

**tzf.pyramid_routing** is a convenience package, that helps loading routing defined and kept in separate list.

Contents
--------

.. toctree::
   :maxdepth: 2

   install
   usage

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`


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
