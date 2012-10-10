# -*- coding: utf-8 -*-

import os.path
import pkgutil


__version__ = '0.0.1'


def add_route(config, route_list):
    '''
        Method adding unpacking routes from route list and adding them to config

        :param pyramid.config.Configurator config: pyramid's app config
        :param list route_list: route lists
    '''
    for route in route_list:
        config.add_route(**route)


def includeme(config):
    '''
        Adds defined routing package into pyramid app

        :param pyramid.config.Configurator config: pyramid's app config
    '''

    # checking for routing package variable
    if 'routing_package' in config.registry.settings:
        routing_package_path = config.registry.settings['routing_package']

        # importing routing package
        routing_package_module = __import__(routing_package_path, fromlist=[routing_package_path])

        # loading submodules
        routing_submodules = [package[1] for package in pkgutil.iter_modules([os.path.dirname(routing_package_module.__file__)]) if not package[2]]

        # we load submodules if any
        for route_submodule in routing_submodules:
            route_submodule = __import__(routing_package_module.__name__ + '.' + route_submodule, fromlist=[routing_package_module.__name__])
            # for each submodule containing a list named routes, we load it, and add routes defined there to config
            if hasattr(route_submodule, 'routes'):
                config.include(lambda config: add_route(config, route_submodule.routes), route_prefix=route_submodule.__name__.split('.')[-1])

        # at the end we add main package paths, to be sure they are at the end of a list in case of a /{variable} route
        add_route(config, routing_package_module.routes)
