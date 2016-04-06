#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('./../'))

import pybush
from pybush.application import application_new, applications_export

my_app = application_new('My Python App',author='Renaud Rubiano',version='0.1.0')
print(my_app)
another_app = application_new('Another Py App')
print(another_app)

import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint
pprint(applications_export())