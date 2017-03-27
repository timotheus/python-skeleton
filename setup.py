from setuptools import setup, find_packages
import re
import os

setup(
    name='{{ project_name }}',
    version='0.0.1',
    description="TODO: Add description",
    author="TODO: Add author",
    author_email="TODO: Add author email",
    url="",
    scripts=['bin/*'],
    packages=find_packages(),
    provides=['{{ project_name }}'],
    install_requires=[line.strip() for line in open('requirements.txt', 'r')],
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ]
)
