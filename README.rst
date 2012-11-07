Introduction:
=============

pyramid_routing is a convenience package, that helps loading routing defined and kept in separate list.

Installation:
=============

pip install pyramid_routing

Configuration:
==============

To configure routing, you have to first include this package in your pyramid app:

.. code-block:: python

    config.include('pyramid_routing')

And add *routing_package* into you settings ini file. This setting should pinpoint the package containing routing.

By default, routing should be defined in package's __init__.py  module and it's submodules in lists of dicts. lists should be named **routes**, and the dict format is the same one as add_route's method.

__init__.py routes definition is read as is, and for convenience, is loaded at the end. This gives the opportunity to add routes catching all possibilities: ``/{match}``

Module-defined routes will be loaded first, with module name as their prefix. if blog.py will contain:

.. code-block:: python

        routes = [
            dict(name='blog:index', pattern='/'),
            dict(name='blog:show', pattern="/show"),
        ]

**blog:index** path will be */blog/*, while **blog:show** will become /blog/show

TODOs:
======

- read from all lists within package (with list name becoming routes prefix)
- read routing from yml configuration


Testing:
========

To run tests, either type ``python setup.py tests`` or ``nosetests --cover-package=tzf.pyramid_routing --cover-tests --with-doctest --with-coverage``
