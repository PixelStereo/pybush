#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import versioneer 
from pylekture._version import get_versions
__version__ = get_versions()['version']
del get_versions
__version__ = __version__.split('+')
__version__ = __version__[0]

setup(
  name = 'pybush',
  packages = ['pybush'],
  version=versioneer.get_version(),
  cmdclass=versioneer.get_cmdclass(),
  description = 'A modular API for building intermedia applications based on a tree graph',
  author = 'Pixel Stereo',
  url='https://github.com/PixelStereo/pybush',
  download_url = 'https://github.com/PixelStereo/pybush/tarball/' + __version__,
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
