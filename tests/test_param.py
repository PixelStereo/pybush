#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

sys.path.append(os.path.abspath('./../'))

import time
import liblo
import datetime
from pybush.constants import __dbug__
from time import sleep
from pybush.functions import m_bool, m_int, m_string, prop_list, prop_dict
from pybush.project import new_project, projects
from pybush.node import Node
from pybush.errors import BushTypeError, NoOutputError
from pprint import pprint
__dbug__ = 4
my_project = new_project(name='My Python project')

# CREATE A DEVICE
my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')
# CREATE AN OUTPUT
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')

supa_param = my_device.new_parameter({'name':'sub/my supa parameter', 'value':-2, 'datatype':'decimal', 'domain':[-2,2], \
                                'clipmode':'both', 'unique':True})

supa_param.snap()
supa_param.value = 5
supa_param.domain = [10,22]
supa_param.clipmode = 'low'
my_device.write('./')