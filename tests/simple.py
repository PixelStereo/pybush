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
from pybush import new_device, get_devices
from pybush.errors import BushTypeError, NoOutputError

from pybush.automation import RampGenerator, RandomGenerator

__dbug__ = 4

def announcement(test):
    print(' ')
    print('---TESTING ' + test + ' -----')
    print(' ')

my_device = new_device(name='My device', author='Pixel Stereo', version='0.1.0')
param2 = my_device.new_parameter({  'name':'node.1',
                                    'value':1,
                                    'datatype':'decimal',
                                    'domain':[0,11], \
                                    'clipmode':'both',
                                    'unique':True,
                                    'tags':['un', 'deux']
                                    })
param3 = my_device.new_parameter({  'name':'node.1/node.2',
                                    'value':-0.5, \
                                    'datatype':'decimal', \
                                    'domain':[-1,1], \
                                    'clipmode':'low', \
                                    'unique':False \
                                    })
parameter = my_device.new_parameter({'name':'/one/two/three/four/five/polo'})
# create two parameters with the same name must be raised
same = my_device.new_parameter({'name':'one/two/three/four/same'})

print(param2.parent)
print(my_device)

snp = param3.snap()
print('--------')
print(snp)
