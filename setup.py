#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

from cidc_ngs_pipeline_api import __author__, __email__, __version__

setup(
    author=__author__,
    author_email=__email__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="The CIDC NGS Pipeline output APIs",
    python_requires=">=3.6",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="cidc_ngs_pipeline_api",
    name="cidc_ngs_pipeline_api",
    packages=find_packages(include=["cidc_ngs_pipeline_api"]),
    test_suite="tests",
    url="https://github.com/CIMAC-CIDC/cidc-ngs-pipeline-api",
    version=__version__,
    zip_safe=False,
)
