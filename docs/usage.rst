Usage
=====

Configuration
-------------

To configure routing, you have to first include this package in your pyramid app:

.. code-block:: python

    config.include('tzf.pyramid_routing')

And add **routing_package** into you settings *ini* file. This setting should pinpoint the package containing routing.

.. code-block:: ini

    [app:main]
        # ....
        routing_package = my.package.lib.routing
        # ....

If You use routing package in other pyramid module, you need this package via normal import:

.. code-block:: python

    from tzf.pyramid_routing import routes_from_package
    routes_from_package(config, 'module.lib.routing')
    config.commit()

.. warning::

    Depending on the order of including plugins, you should add config.commit() between pyramid_routing inclusion, and the other module, that uses it.

    Although, It doesn't give errors in all cases. Investigation is needed.

Defining routes
---------------

By default, routing should be defined in package's *__init__.py*  module and it's submodules in lists of dicts. lists should be named **routes**, and the dictionary format is the same one as pyramid's **config.add_route**'s method.

*__init__.py* routes definition is read as is, and for convenience, is loaded at the end. This gives the opportunity to add routes catching all possibilities: ``/{match}``

Module-defined routes will be loaded first, with module name as their prefix. If blog.py will contain:

.. code-block:: python

    routes = [
        {'name': 'blog:index', 'pattern':'/'},
        {'name':'blog:show', 'pattern':'/show'},
    ]

**blog:index** path will be */blog/*, while **blog:show** will become /blog/show

Redefining route prefix
+++++++++++++++++++++++

Route prefix for routing submodules reflects the submodule name. But if you require some more fancy name (Possibly a variable, that is beeing set by default), you can do so, by defining a prefix variable on that module:

.. code-block:: python

    prefix = '{locale}/blog'

    routes = [
        {'name': 'blog:index', 'pattern':'/'},
        {'name':'blog:show', 'pattern':'/show'},
    ]

**blog:index** path now will be *{locale}/blog/*, while **blog:show** will become {locale}/blog/show. Of course, the /blog part in prefix can be totally missed.
