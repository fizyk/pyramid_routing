from pytest_pyramid import factories

clean_config = factories.pyramid_config({})

simplerouting_config = factories.pyramid_config({
    'routing_package': 'tests.routes_definitions.routing',
    'pyramid.includes': ['tzf.pyramid_routing']
})

moduled_config = factories.pyramid_config({
    'routing_package': 'tests.routes_definitions.routing_moduled',
    'pyramid.includes': ['tzf.pyramid_routing']
})

two_moduled_config = factories.pyramid_config({
    'routing_package': 'tests.routes_definitions.routing_two_moduled',
    'pyramid.includes': ['tzf.pyramid_routing']
})


prefixed_config = factories.pyramid_config({
    'routing_package': 'tests.routes_definitions.routing_prefixed',
    'pyramid.includes': ['tzf.pyramid_routing']
})
