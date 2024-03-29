#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on mptt.VERSION
version_tuple = (0, 1, 0, 'alpha', 0)
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'shoppinglist',
    description = '''A tool for keeping track of the levels of things in a
        shared office fridge.''',
    version = version,
    author = 'Texas Tribune',
    url = 'http://github.com/texastribune/shoppinglist',
    packages=['shoppinglist'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)

