from setuptools import find_packages
from setuptools import setup


setup(
    name='aoc',
    version='0.0.1',
    author='mchlrhw',
    packages=find_packages(),
    setup_requires=[
        'hypothesis',
        'pytest-cov',
        'pytest-flake8',
        'pytest-mypy',
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
