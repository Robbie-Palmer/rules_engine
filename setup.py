from setuptools import setup, find_packages

setup(
    name='rules_engine',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    setup_requires=['wheel']
)
