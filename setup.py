from setuptools import setup, find_packages

long_description = (
    'This project contains library functions for converting '
    'between the Unit Address and MAC address representations of SCTE 55-1 '
    'terminals, e.g. Motorola-brand set-top boxes and CableCARDs.'
)

setup(
    name='scte_55-1_address',
    version='2015.2.15',
    license='MIT',
    url='https://github.com/bbayles/scte_55-1_address',

    description='SCTE 55-1 terminal identifier converters',
    long_description=(
        'Library for working with SCTE 55-1 terminal identifiers'
    ),

    author='Bo Bayles',
    author_email='bbayles@gmail.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='scte cable settop cablecard',

    packages=find_packages(),
    test_suite='tests',
)
