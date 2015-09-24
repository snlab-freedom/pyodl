# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='python-odl',
    version='0.0.1',
    author='Beraldo Leal',
    author_email='beraldo@ncc.unesp.br',
    packages=find_packages(exclude=['test', 'bin', 'scripts']),
    url='http://github.com/beraldoleal/python-odl/',
    license='LICENSE.md',
    description='Python 2.x library for OpenDayLight interations via REST API.',
    install_requires=install_requires,
    scripts=[],
)
