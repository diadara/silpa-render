#!/usr/bin/env python

from setuptools import setup, find_packages

name = "render"

setup(
    name=name,
    version="0.2.1",
    url="http://silpa.org.in/NGram",
    license="LGPL-3.0",
    description="Convert wiki pages to pdf and text into images",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""Convert wiki pages to pdf and text into images""",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    test_suite='tests',
    install_requires=['setuptools', 'hyphenation', 'pypdflib', 'pyquery','PIL'],
    zip_safe=False,
)
