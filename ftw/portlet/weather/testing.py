from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import setRoles, TEST_USER_ID, TEST_USER_NAME, login
from zope.configuration import xmlconfig


class FtwWeatherPortletLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ftw.portlet.weather

        xmlconfig.file(
            'configure.zcml', ftw.portlet.weather,
                context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ftw.portlet.weather:default')

        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

FTW_WEATHERPORTLET_FIXTURE = FtwWeatherPortletLayer()
FTW_WEATHERPORTLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FTW_WEATHERPORTLET_FIXTURE,), name="FtwWeatherPortletLayer:Integration")
