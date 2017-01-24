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

__dbug__ = 4


my_device = new_device(name='My device', author='Pixel Stereo', version='0.1.0')

another_device = new_device(name='My device', author='Stereo Pixel', version='0.1.1')
print('how many devices : ' + str(len(get_devices())))
print('----------------------------------------------------------------------')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
midi_output = my_device.new_output(protocol='MIDI')
print('how many outputs for my_device : ' + str(len(my_device.outputs)))
#print('how many inputs for my_device : ' + str(len(my_device.inprint('how many outputs for my_device : ' + str(len(my_device.outputs)))puts)))
print('----------------------------------------------------------------------')

node_1 = my_device.new_child(name='node.1')
node_1.parameter = {
                    'name':'node.1',
                    'value':1,
                    'datatype':'decimal',
                    'domain':[0,11],
                    'clipmode':'both',
                    'unique':True
                    }
my_device.new_parameter({'name':'node.1/node.2/param'})

node_1.parameter.snap()
node_1.parameter.value = 2
node_1.parameter.name= 'replace'
node_1.parameter.domain = [2, 22]
node_1.parameter.datatype = 'integer'
node_1.parameter.clipmode = 'low'
node_1.parameter.unique = False

print(my_device.write('./'))
print('______reading file : ' + str(another_device.read('./My device.bush')))
print('----------------------------------------------------------------------')


print('----------------------------------------------------------------------')
print(my_device.output)
print('----------------------------------------------------------------------')
print(my_device.children[0].parameter)
print(my_device.children[0].parameter.recall(my_device.children[0].parameter.snapshots[0]))
print(my_device.children[0].parameter)
print('----------------------------------------------------------------------')
print(my_device.children[0].parameter.snapshots[0])
print('----------------------------------------------------------------------')
print(another_device)
print('----------------------------------------------------------------------')
another_device.name = 'new one'
#print(another_device)
print('----------------------------------------------------------------------')
print(another_device.write('./'))
