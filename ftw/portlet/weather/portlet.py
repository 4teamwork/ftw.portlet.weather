from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from plone.memoize.compress import xhtml_compress
from zope.interface import implements
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from ftw.portlet.weather import _


class IWeatherPortlet(IPortletDataProvider):
    """Weather portlet Interface
    """


class Assignment(base.Assignment):
    implements(IWeatherPortlet)

    def __init__(self, *args, **kwargs):
        super(Assignment, self).__init__(self, *args, **kwargs)

    @property
    def title(self):
        return _(u"SF meteo weather portlet")


class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def get_swf_url(self):
        registry = getUtility(IRegistry)
        if 'ftw.portlet.weather.url' not in registry:
            return None
        return registry['ftw.portlet.weather.url']

    def render(self):
        return xhtml_compress(self._template())


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
