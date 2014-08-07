from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        """
		Prevents all profiles but 'default' from showing up in the
		profile list when creating a Plone site.
		"""
        return [
            u'uwosh.snippets:uninstall',
        ]


def setupVarious(context):

    site = context.getSite()