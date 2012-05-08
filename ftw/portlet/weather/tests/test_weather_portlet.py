from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from zope.component import getUtility, getMultiAdapter
from Products.GenericSetup.utils import _getDottedName
from ftw.portlet.weather import portlet as weather
from ftw.portlet.weather.testing import (
    FTW_WEATHERPORTLET_INTEGRATION_TESTING)
import unittest2 as unittest
from plone.registry.interfaces import IRegistry


class TestPortlet(unittest.TestCase):
    """Test weather portlet
    """

    layer = FTW_WEATHERPORTLET_INTEGRATION_TESTING

    def test_portlet_type_registered(self):
        portlet = getUtility(
            IPortletType, name='ftw.portlet.weather')
        self.assertEquals(
            portlet.addview, 'ftw.portlet.weather')

    def test_registered_interfaces(self):
        portlet = getUtility(
            IPortletType, name='ftw.portlet.weather')
        registered_interfaces = [_getDottedName(i) for i in portlet.for_]
        registered_interfaces.sort()
        self.assertEquals(
            ['zope.interface.Interface', ], registered_interfaces)

    def test_interfaces(self):
        portlet = weather.Assignment()
        self.failUnless(
            weather.IWeatherPortlet.providedBy(portlet))

    def test_renderer(self, section=''):
        context = self.layer['portal']
        request = self.layer['request']
        view = context.restrictedTraverse('@@plone')
        manager = getUtility(
            IPortletManager, name='plone.rightcolumn', context=context)
        assignment = weather.Assignment()
        renderer = getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)
        self.assertTrue("weather" in renderer.render())
        registry = getUtility(IRegistry)
        self.assertTrue(
            registry['ftw.portlet.weather.url'] in renderer.render())

    def test_assignment(self):
        assignment = weather.Assignment()
        self.assertEqual(
            assignment.title,
            u'SF meteo weather portlet')
