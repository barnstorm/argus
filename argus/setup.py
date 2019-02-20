#!/usr/bin/python

description = '''
Argus, general rpg framework
'''

from setuptools import setup

setup(
    name='argus',
    package_dir={'': '.'},
    version='0.0.1',
    description=description,
    long_description=description,
    author="barnstorm",
    author_email="bill@armstravaganza.com",
    packages=['lib','models'],
    setup_requires=[
        "setuptools"
    ],
    install_requires=[
    ],
    dependency_links=[
    ]
)