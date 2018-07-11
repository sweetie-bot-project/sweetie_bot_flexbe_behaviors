#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages = ['behavior_derpfest2017presentation'],
    package_dir = {'': 'src'}
)

setup(**d)