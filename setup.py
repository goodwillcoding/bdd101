import os
import sys

from setuptools import setup
from setuptools import find_packages

README = CHANGES = ''

install_requires=[]

tests_require = [
    'nose2',
    'planterbox',
    ]

setup(name='bdd101',
      version='1.0dev0',
      description='BDD101',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='',
      author="",
      author_email="",
      packages=find_packages(),
      zip_safe=False,
      install_requires = [],
      tests_require = tests_require,
      test_suite="bdd101.tests",
      )

