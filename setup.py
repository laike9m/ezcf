# coding: utf-8
import os

import codecs
from setuptools import setup, find_packages

def read():
    """Build a file path from *paths* and return the contents."""
    with codecs.open(os.path.join('README.rst'), 'r', "utf-8") as f:
        return f.read()

setup(
    name='ezcf',
    version='0.0.1post1',
    description='Import JSON/YAML like importing .py files',
    long_description=read(),
    url='http://github.com/laike9m/ezcf/',
    license='MIT',
    author='laike9m',
    author_email='laike9m@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': ['README.md']},
    keywords = ['config', 'import'],
    install_requires=['pyyaml'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)