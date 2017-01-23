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
from pybush import new_device
from pybush.node import Node
from pybush.errors import BushTypeError, NoOutputError

__dbug__ = 4

# CREATE A DEVICE
my_device = new_device(name='My device', author='Pixel Stereo', version='0.1.0')
# CREATE AN OUTPUT
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')

supa_param = my_device.new_parameter({'name':'sub/my supa parameter', 'value':-2, 'datatype':'decimal', 'domain':[-2,2], \
                                'clipmode':'both', 'unique':True})
print('-----------')
snap = supa_param.snap()
supa_param.domain = [0.5, 0.8]
supa_param.value = 0.123456789
supa_param.clipmode = 'low'
supa_param.unique = False
my_device.write('./')
