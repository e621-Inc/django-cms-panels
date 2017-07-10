# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
from cms_panels import __version__


try:
    from pypandoc import convert
except ImportError:
    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


DESCRIPTION = 'Django-CMS plugin with info on image'
CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 4 - Beta',
]


setup(
    name='django-cms-panels',
    version=__version__,
    author='Alaric Mägerle',
    author_email='info@rouxcode.ch',
    description=DESCRIPTION,
    long_description='',
    url='https://github.com/rouxcode/django-cms-panels',
    license='MIT',
    keywords=['django'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[],
    packages=find_packages(exclude=['example', 'docs']),
    include_package_data=True,
    zip_safe=False,
)
