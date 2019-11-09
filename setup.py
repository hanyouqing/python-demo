# -*- coding: utf-8 -*-

# from setupools import setup
# from distutils.core import setup
import setuptools
import platform

NAME                = 'demo-python'
VERSION             = '0.0.1'
DESCRIPTION         = 'A demo project for python'
URL                 = 'https://github.com/icmdb/demo-python',
AUTHOR              = 'icmdb'
AUTHOR_EMAIL        = 'demo@icmdb.vip'
MAINTAINER          = 'icmdb'
MAINTAINER_EMAIL    = 'demo@icmdb.vip'
LICENSE             = 'MIT'
LONG_DESCRIPTION    = open('README.md').read()
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
KEYWORDS            = 'python, demo, pydemo, package, setup'
PLATFORMS           = ''
STATUS              = "5 - Production/Stable"
CLASSIFIERS         = [
        'Development Status :: %s' % (STATUS),
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: %s License' % (LICENSE),
        'Programming Language :: Python :: %s' % (platform.python_version()),
    ]

PACKAGES            = setuptools.find_packages()
PY_MODULES          = ['demo', 'demoutils']
SCRIPTS             = [
    'demoutils/demoutils'
]
#INCLUDE_PACKAGE_DATA = True
#INSTALL_REQUIRES = []
#ENTRY_POINTS = {
#    "console_scripts": [
#        "demo = demo-python.demo:main",
#    ]
#}
ENTRY_POINTS ="""
    [console_scripts]
    demo=demo:cli
"""

setuptools.setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    url = URL,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    maintainer = MAINTAINER,
    maintainer_email = MAINTAINER_EMAIL,
    license = LICENSE,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = LONG_DESCRIPTION_CONTENT_TYPE,
    keywords = KEYWORDS,
    platforms = PLATFORMS,
    classifiers = CLASSIFIERS,

    packages = PACKAGES,
    py_modules = PY_MODULES,
    #scripts = SCRIPTS,
    #include_package_data = INCLUDE_PACKAGE_DATA,
    #install_requires = INSTALL_REQUIRES,
    #entry_points = ENTRY_POINTS,
)
