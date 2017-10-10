# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
description = 'Effective Dimensionality Reduction based on Gaussian Processes'

setup(
    name='edr-gp',
    version='0.0.1',
    description=description,
    long_description=long_description,
    url='https://github.com/neuro-ml/edr-gp',
    author='Neuro.ml group',
    author_email='belyaevmichel+edr-gp@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5',
    ],
    packages=['edr-gp'],
    install_requires=['GPy, scikit-learn'],
)