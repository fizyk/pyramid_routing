# -*- coding: utf-8 -*-

# Copyright (c) 2013 by tzf.pyramid_routing authors and contributors <see AUTHORS file>
#
# This module is part of tzf.pyramid_routing and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT

import os.path
import pkgutil
from pyramid.path import package_of


__version__ = '0.1.1'


def add_routes(configurator, route_list):
    '''
        Method adding unpacking routes from route list and adding them to configurator

        :param pyramid.config.Configurator configurator: pyramid's app configurator
        :param list route_list: route lists
    '''
    for route in route_list:
        configurator.add_route(**route)


def includeme(configurator):
    '''
        Adds rotues defined in config into pyramid app

        :param pyramid.config.Configurator configurator: pyramid's app configurator
    '''

    routes_from_package(configurator, configurator.registry.settings['routing_package'])


def routes_from_package(configurator, routing_package_path):
    '''
        Adds defined routing package into pyramid app

        :param pyramid.config.Configurator configurator: pyramid's app configurator
        :param str routing_package_path: routing package to include
    '''

    if routing_package_path is not None:
        # importing routing package
        routing_package_module = __import__(routing_package_path,
                                            fromlist=[routing_package_path.rsplit('.')[0]])

        # loading submodules
        routing_submodules = [package[1] for package in pkgutil.iter_modules([os.path.dirname(routing_package_module.__file__)]) if not package[2]]

        # we load submodules if any
        for route_submodule in routing_submodules:
            route_submodule = __import__(routing_package_module.__name__ + '.' + route_submodule,
                                         fromlist=[routing_package_module.__name__])
            # for each submodule containing a list named routes, we load it, and add routes defined there to config
            if hasattr(route_submodule, 'routes'):
                # actually borrowing some code from Configurator's.includeme

                if hasattr(route_submodule, 'prefix'):
                    route_prefix = route_submodule.prefix
                else:
                    route_prefix = route_submodule.__name__.split('.')[-1]

                sub_configurator = configurator.__class__(
                    registry=configurator.registry,
                    package=package_of(route_submodule),
                    autocommit=configurator.autocommit,
                    route_prefix=route_prefix,
                )
                add_routes(sub_configurator, route_submodule.routes)

        # at the end we add main package paths, to be sure they are at the end of a list in case of a /{variable} route
        add_routes(configurator, routing_package_module.routes)
