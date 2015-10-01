#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.chatterbox',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.chatterbox'],
    version='0.1',
    description='Python tools for Who\'s On First notifications',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-chatterbox',
    install_requires=[
        'redis',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-chatterbox/releases/tag/v0.1',
    license='BSD')
