from tzf.pyramid_routing import routes_from_package


def includeme(config):
    '''
        Full includeme
    '''
    routes_from_package(config, 'tzf.pyramid_routing.tests.routing_to_include_2')
