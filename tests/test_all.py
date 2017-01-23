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
from pybush.errors import BushTypeError, NoOutputError

__dbug__ = 4

my_project = new_project(name='My Python project')
print('how many projects : ' + str(len(projects())))

my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')
another_device = my_project.new_device(name='My device', author='Stereo Pixel', version='0.1.1')
print('how many devices : ' + str(len(my_project.devices)))

output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
midi_output = my_device.new_output(protocol='MIDI')
print('how many outputs for my_device : ' + str(len(my_device.outputs)))

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
print('----------------------------------------------------------------------')
print('this is the node_1 : ')
print('----------------------------------------------------------------------')
print(node_1)
print('----------------------------------------------------------------------')
print('this is the parameter of the node_1 : ')
print('----------------------------------------------------------------------')
print(node_1.parameter)
print('----------------------------------------------------------------------')
node_2 = my_device.new_parameter({
                                    'name':'node.2',
                                    'value':2,
                                    'datatype':'decimal',
                                    'domain':[0,22],
                                    'clipmode':'both',
                                    'unique':True
                                    })
print('----------------------------------------------------------------------')
print('this is the parameter of the node_2 : ')
print('----------------------------------------------------------------------')
print(node_2)
print('----------------------------------------------------------------------')
print('and the node of the parameter : ')
print('----------------------------------------------------------------------')
print(node_2.parent)

print()
print(type(node_1.export()))
print(node_2.export())
quit()

node_2 = node_1.new_child(name='node.2', tags=['lol', 'lal'])
node_3 = node_2.new_child(name="node.3")

node_1.tags=['init', 'video']
print(param2)
param3 = my_device.new_parameter({  'name':'node.1/node.2',
                                    'value':-0.5, \
                                    'datatype':'decimal', \
                                    'domain':[-1,1], \
                                    'clipmode':'low', \
                                    'unique':False \
                                    })

        self.assertEqual(node_1.write(node1_write_path), True)
print(param3)
print('----')
print(node_1)

"""snap_device = my_device.new_snapshot()
snap_project = my_project.new_snapshot()
param2.value = 0
param2.ramp(1, 500)
param3.value = 1
param3.datatype = 'decimal'
param3.ramp(0, 500)
sleep(0.5)
param3.domain = [0.4, 0.6]
param3.random(destination=1, duration=700)
param3.value = 0.5
param2.ramp(0, 500)
sleep(0.7)
param2.value = 1"""

