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
from pybush.node import Node
from pybush.errors import BushTypeError, NoOutputError

__dbug__ = 4
# CREATE A DEVICE
my_device = new_device(name='My device', author='Pixel Stereo', version='0.1.0')
# CREATE AN OUTPUT
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')


oda_param = my_device.new_parameter({'name':'sub/device/lala/menu', 'datatype':'integer', 'domain':[0,50], 'clipmode':'low'})

supa_param = my_device.new_parameter({'name':'my supa parameter', 'value':-2, 'datatype':'decimal', 'domain':[-2,2], \
                                'clipmode':'both', 'unique':True})

"""print('address of supa_param', supa_param.address)
print('------------------')
print('address of oda_param', oda_param.address)
print('------------------')
print('------------------')
print('CHILDREN', len(my_device.children))
print('------------------')
print('------------------')
print('address of my_device : ' + my_device.address, my_device.parameter)
print('address of the first child of my_device : ' + my_device.children[0].address, my_device.children[0].parameter)
print('address of the first child of the first child of my_device : ' + my_device.children[0].children[0].address, my_device.children[0].children[0].parameter)
print('address of the first child of the first child of the first child of my_device : ' + my_device.children[0].children[0].children[0].address, my_device.children[0].children[0].children[0].parameter)
print(len(my_device.children[0].children))"""
#supa_param.ramp(2, 100)
print('-----------')
snap = supa_param.snap()
supa_param.domain = [0.5, 0.8]
supa_param.value = 0.123456789
supa_param.clipmode = 'low'
supa_param.unique = False
snap2 = supa_param.snap()
print(supa_param.value)
supa_param.recall(snap)
print(supa_param.value)
print('the snap', snap)
#print(prop_dict(snap))
my_device.write('./')
#print(my_device)
print('-----WWWWWWWW------')
new_device = new_device()
device_import = new_device.load('./My Device.bush')
print('--------------')
print('--------------')
#print(device_import)
#print(new_device)

