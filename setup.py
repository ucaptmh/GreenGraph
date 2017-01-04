#!/usr/bin/env python
__author__ = 'third'
from setuptools import setup, find_packages
setup(
    name = "Greengraph",
    version ="0.1.0",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    entry_points=dict(console_scripts=[
        'greengraph = greengraph.__main__:process']),
    install_requires = ['argparse', 'matplotlib', 'numpy', 'requests', 'geopy']
)