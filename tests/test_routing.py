import pytest
from pyramid.interfaces import IRoutesMapper


@pytest.mark.parametrize('config_fixture, route_count', (
    ('simplerouting_config', 3),
    ('moduled_config', 6),
    ('two_moduled_config', 9),
    ('prefixed_config', 9)
))
def test_read_count(request, config_fixture, route_count):
    '''A test to read routes from python package'''

    config = request.getfuncargvalue(config_fixture)

    # actually needed to be able tu use getUtility
    config.commit()

    mapper = config.registry.getUtility(IRoutesMapper)
    routes = mapper.get_routes()
    assert len(routes) > 0
    assert len(routes) == route_count


@pytest.mark.parametrize('config_fixture, route_number, name, pattern', (
    ('simplerouting_config', 0, 'index', '/'),
    ('moduled_config', 0, 'module_index', 'module/'),
    ('moduled_config', 3, 'index', '/'),
    ('two_moduled_config', 0, 'module_index', 'module/'),
    ('two_moduled_config', 3, 'second_index', 'second/'),
    ('two_moduled_config', 4, 'second_secret', 'second/secret'),
    ('two_moduled_config', 6, 'index', '/'),
    ('prefixed_config', 0, 'module_index', '{var}/'),
    ('prefixed_config', 1, 'module_secret', '{var}/secret'),
    ('prefixed_config', 3, 'second_index', '{var}/subpath/'),
    ('prefixed_config', 4, 'second_secret', '{var}/subpath/secret'),
))
def test_routename(request, config_fixture, route_number, name, pattern):
    '''A test to check whether index is the first route'''

    config = request.getfuncargvalue(config_fixture)

    # actually needed to be able tu use getUtility
    config.commit()

    mapper = config.registry.getUtility(IRoutesMapper)
    routes = mapper.get_routes()
    assert routes[route_number].name == name
    assert routes[route_number].pattern == pattern


def test_by_hand_only(clean_config):
    '''run includeme by hand'''
    config = clean_config
    config.commit()
    from tzf.pyramid_routing import routes_from_package

    routes_from_package(config, 'tests.routes_definitions.routing')

    config.commit()


def test_includeme_and_by_hand(simplerouting_config):
    '''config.include and by hand in app'''

    config = simplerouting_config
    config.commit()

    from tzf.pyramid_routing import routes_from_package

    routes_from_package(config, 'tests.routes_definitions.routing_moduled')

    config.commit()


def test_includeme_and_by_hand_with_includeme_ab(simplerouting_config):
    '''config.include in app, and two includeme's in other 'plugin' '''

    config = simplerouting_config
    config.commit()

    config.include('tzf.pyramid_routing')

    config.include('tests.routes_definitions.module_to_include_1')
    config.include('tests.routes_definitions.module_to_include_2')

    config.commit()


def test_includeme_and_by_hand_with_includeme(simplerouting_config):
    '''config.include in app, and includeme in other 'plugin' '''

    config = simplerouting_config
    config.commit()

    def includeme_test(config):
        '''
            Method for testing includeme
        '''
        from tzf.pyramid_routing import routes_from_package
        routes_from_package(config, 'tests.routes_definitions.routing_moduled')

    config.include(includeme_test)
    config.commit()
    config.include('tzf.pyramid_routing')
    config.commit()
