# -*- coding: utf-8 -*-

import os.path
import pkgutil


__version__ = '0.0.1'


def add_route(config, route_list):
    for route in route_list:
        config.add_route(**route)


def includeme(config):
    '''
        Adds defined routing package into pyramid app
    '''

    if 'routing_package' in config.registry.settings:
        routing_package_path = config.registry.settings['routing_package']

    routing_package_module = __import__(routing_package_path, fromlist=[routing_package_path])

    routing_submodules = [package[1] for package in pkgutil.iter_modules([os.path.dirname(routing_package_module.__file__)]) if not package[2]]

    for route_submodule in routing_submodules:
        route_submodule = __import__(routing_package_module.__name__ + '.' + route_submodule, fromlist=[routing_package_module.__name__])
        if hasattr(route_submodule, 'routes'):
            config.include(lambda config: add_route(config, route_submodule.routes), route_prefix=route_submodule.__name__.split('.')[-1])

    # at the end we add main package paths, to be sure they are at the end of a list in case of a /{variable} route
    add_route(config, routing_package_module.routes)
