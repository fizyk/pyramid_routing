# -*- coding: utf-8 -*-

import unittest
from pyramid.exceptions import ConfigurationConflictError

try:  # pragma: no cover
    from webtest import TestApp
except ImportError:  # pragma: no cover
    pass


from pyramid.interfaces import IRoutesMapper


def config_factory(**settings):
    """Call with settings to make and configure a configurator instance,
      binding to an in memory db.
    """

    from pyramid.config import Configurator

    # Initialise the ``Configurator`` and setup a session factory.
    config = Configurator(settings=settings)
    # Include pyramid_routing
    config.include('tzf.pyramid_routing')
    # Return the configurator instance.
    return config


class BaseTestCase(unittest.TestCase):  # pragma : no-cover

    def setUp(self, routing_package):
        """Configure the Pyramid application."""

        settings = {'routing_package': routing_package}
        self.config = config_factory(**settings)

        self.app = TestApp(self.config.make_wsgi_app())

    def tearDown(self):
        """Make sure the session is cleared between tests."""


class TestSimpleroutingPackage(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self, 'tzf.pyramid_routing.tests.routing')

    def test_read(self):
        """A test to read routes from python package"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertTrue(len(routes), 'There should be routes!')
        self.assertEqual(3, len(routes), 'There should be three routes')

    def test_first(self):
        """A test to check whether index is the first route"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(routes[0].name, 'index', 'index route is not the first defined!')


class TestPackagedRouting(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self, 'tzf.pyramid_routing.tests.routing_moduled')

    def test_read(self):
        """A test to read routes from python package with modules"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertTrue(len(routes), 'There should be routes!')
        self.assertEqual(6, len(routes), 'There should be six routes defined, you have {0}'.format(len(routes)))

    def test_module_prefixed_name(self):
        """A test to read routes from python package with modules"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(routes[0].name, 'module_index', 'There should be three routes')

    def test_main_routes(self):
        """A test to check whether main routes are added at the end"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(routes[3].name, 'index', 'index route is not the fourth defined! - first of the last batch')


class TestNoIncludeMeRouting(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self, 'tzf.pyramid_routing.tests.routing_two_moduled')

    def test_read(self):
        """A test to read routes from python package with 2 modules"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertTrue(len(routes), 'There should be routes!')
        self.assertEqual(9, len(routes), 'There should be nine routes defined, you have {0}'.format(len(routes)))

    def test_module_prefixed_name(self):
        """A test to read routes from python package with 2 modules"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(routes[3].name, 'second_index', 'There should be three routes')

    def test_main_routes(self):
        """A test to check whether main routes are added at the end with more than one additional module"""
        mapper = self.config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(routes[6].name, 'index', 'index route is not the fourth defined! - first of the last batch')


class TestSimpleRoutingByHand(BaseTestCase):

    def setUp(self):
        """Configure the Pyramid application."""

        from pyramid.config import Configurator

        # Initialise the ``Configurator`` and setup a session factory.
        self.config = Configurator(settings={})

    def test_by_hand_only(self):
        """run includeme by hand"""

        from tzf.pyramid_routing import routes_from_package

        try:
            routes_from_package(self.config, 'tzf.pyramid_routing.tests.routing')

            self.app = TestApp(self.config.make_wsgi_app())
        except ConfigurationConflictError as e:
            self.fail(e)

    def test_includeme_and_by_hand(self):
        """config.include and by hand in app"""

        from pyramid.config import Configurator

        # Initialise the ``Configurator`` and setup a session factory.
        self.config = Configurator(settings={'routing_package': 'tzf.pyramid_routing.tests.routing'})

        try:
            self.config.include('tzf.pyramid_routing')

            from tzf.pyramid_routing import routes_from_package

            routes_from_package(self.config, 'tzf.pyramid_routing.tests.routing_moduled')

            self.app = TestApp(self.config.make_wsgi_app())
        except ConfigurationConflictError as e:
            self.fail(e)

    def test_includeme_and_by_hand_with_includeme_ab(self):
        """config.include in app, and includeme in other 'plugin' """

        from pyramid.config import Configurator

        # Initialise the ``Configurator`` and setup a session factory.
        self.config = Configurator(settings={'routing_package': 'tzf.pyramid_routing.tests.routing'})

        try:

            self.config.include('tzf.pyramid_routing')

            self.config.include('tzf.pyramid_routing.tests.module_to_include_1')
            self.config.include('tzf.pyramid_routing.tests.module_to_include_2')
            self.app = TestApp(self.config.make_wsgi_app())

        except ConfigurationConflictError as e:
            self.fail(e)

    def test_includeme_and_by_hand_with_includeme(self):
        """config.include in app, and includeme in other 'plugin' """

        from pyramid.config import Configurator

        # Initialise the ``Configurator`` and setup a session factory.
        self.config = Configurator(settings={'routing_package': 'tzf.pyramid_routing.tests.routing'})

        def includeme_test(config):
            '''
                Method for testing includeme
            '''
            from tzf.pyramid_routing import routes_from_package
            routes_from_package(config, 'tzf.pyramid_routing.tests.routing_moduled')

        try:
            self.config.include(includeme_test)
            self.config.commit()
            self.config.include('tzf.pyramid_routing')

            self.app = TestApp(self.config.make_wsgi_app())
        except ConfigurationConflictError as e:
            self.fail(e)
