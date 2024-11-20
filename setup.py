from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculator=calculator:main',
        ],
    },
)