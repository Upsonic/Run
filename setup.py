#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="upsonic_run",
    version="0.1.1",
    description="""The cloud python function runner !""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Upsonic/Upsonic-Run",
    author="Onur Atakan ULUSOY",
    author_email="atadogan06@gmail.com",
    license="MIT",
    packages=["upsonic_run",],
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)


