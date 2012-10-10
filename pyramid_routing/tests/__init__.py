# -*- coding: utf-8 -*-

import unittest

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
    # Include simpleauth.
    config.include('pyramid_routing')
    # Return the configurator instance.
    return config


class BaseTestCase(unittest.TestCase):  # pragma : no-cover

    def setUp(self, routing_package):
        """Configure the Pyramid application."""

        settings = dict(routing_package=routing_package)
        self.config = config_factory(**settings)

        self.app = TestApp(self.config.make_wsgi_app())

    def tearDown(self):
        """Make sure the session is cleared between tests."""


class TestSimpleroutingPackage(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self, 'pyramid_routing.tests.routing')

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
        BaseTestCase.setUp(self, 'pyramid_routing.tests.routing_moduled')

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
