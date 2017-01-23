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
from pprint import pprint

__dbug__ = 4
new_device = new_device()
device_import = new_device.load('./My Device.bush')
"""print('--------------')
print('IMPORT', device_import)
print('--------------')
print(type(new_device))
print('--------------')
print(new_device.name)
print('--------------')
print(new_device.name)
print(len(new_device.children))
child = new_device.children[0]
print('--------------')
print(child)
print('--------------')
print(new_device)
print('--------------')
print('--------------')
print('--------------')
print('--------------')
print('--------------')
print('--------------')"""
#pprint(new_device.export())
#pprint(new_device.children[0].parameter.export())
#print(type(new_device.children[0].parameter))

print('x')
#print(device_import)
pprint(prop_dict(new_device))


quit()



print(type(new_device.children[0].parameter.snapshots[0]))
print(new_device.children[0].parameter.snapshots)
new_device.name = 'new device'
print(new_device.write('./'))
print('--------------')
#print(device_import)
#print(new_device)

