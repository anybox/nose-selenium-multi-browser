# -*- coding: utf-8 -*-
import io
from setuptools import setup


def parse_requirements(file):
    required = []
    with open(file) as f:
        for req in f.read().splitlines():
            if not req.strip().startswith('#'):
                required.append(req)
    return required


def read(*args, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in args:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


requires = parse_requirements('requirements.txt')
long_description = read('README.rst', 'CHANGES.rst')

setup(
    name='nose-selenium-multi-browser',
    version='0.0.1',
    description='nose-selenium-multi-browser is a plugin for nose that provides'
                ' support to launch selenium tests in parallels on multiple '
                'browsers.',
    long_description=long_description,
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/anybox/nose-selenium-multi-browser',
    packages=[
        'nose_selenium_multi_browser',
        'nose_selenium_multi_browser.plugins',
    ],
    install_requires=requires,
    dependency_links=[
        'git+https://github.com/anybox/selenium-configurator.git@develop#'
        'egg=selenium-configurator',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'selenium = nose_selenium_multi_browser.plugins.selenium:Selenium'
        ]
    },
    license='LGPL-3.0',
    keywords='nose selenium CI',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)
