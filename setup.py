import os
from setuptools import setup, find_packages


version = '1.0.3.dev0'
mainainter = 'Mathias Leimgruber'

tests_require = ['plone.app.testing',]

setup(name='ftw.portlet.weather',
      version=version,
      description="Shows the sf meteo weather forcast",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='ftw portlet weather',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.portlet.weather',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw', 'ftw.portlet', ],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'ftw.upgrade>=1.14',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
