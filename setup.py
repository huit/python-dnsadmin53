#!/usr/bin/env python

from setuptools import setup
import os


setup(
    name         = 'dnsadmin53',
    version      = '0.0.1',
    url          = 'https://github.com/huit/python-dnsadmin53',
    description  = 'DNS Admin tool for Route53 IAM/ARN Managment',
    packages     = ['dnsadmin53'],
    author       = 'Harvard University Information Technology',
    author_email = 'ithelp@harvard.edu',
    license      = 'LICENSE',
    install_requires = [
        'argparse>=1.2',
        'boto>=2.0',
        'PyYAML',
        'termcolor',
        'colorama',
    ],
    setup_requires = [
        'setuptools_git>=1.0',
        'pypandoc>=0.7.0',
    ],
    test_suite = 'nose.collector',
    tests_require = [
        'flake8>=2.1.0',
        'nose>=1.3.0',
        'coverage>=3.7',
    ],
)
