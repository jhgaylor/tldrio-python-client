import os
from setuptools import setup, find_packages

setup(
    name = "tldr-python-client",
    version = "0.1",
    author = "Jake Gaylor",
    author_email = "jake@codegur.us",
    description = "An api wrapper for http://tldr.io/",
    url = "https://github.com/jhgaylor/tldrio-python-client",
    install_requires = [ln for ln in open('requirements.txt')],
    packages = find_packages(), 
    include_package_data = True,
)