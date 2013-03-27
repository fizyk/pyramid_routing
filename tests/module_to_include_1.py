from tzf.pyramid_routing import routes_from_package


def includeme(config):
    '''
        Full includeme
    '''
    routes_from_package(config, 'tests.routing_to_include_1')
