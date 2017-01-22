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

another_project = new_project('Another Python project')
#len(projects())
my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')
another_device = my_project.new_device(name='My device', author='Stereo Pixel', version='0.1.1')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
midi_output = my_device.new_output(protocol='MIDI')
node_1 = my_device.new_child(name='node.1')
node_2 = node_1.new_child(name='node.2', tags=['lol', 'lal'])
node_3 = node_2.new_child(name="node.3")
param1 = my_device.make_parameter()
param2 = my_device.new_parameter({'name':'node.1', 'value':1, 'datatype':'decimal', 'domain':[0,11], \
                                'clipmode':'both', 'unique':True})
node_1.tags=['init', 'video']
print('param2', param2)
param3 = my_device.new_parameter({  'name':'node.1/node.2',
                                    'value':-0.5, \
                                    'datatype':'decimal', \
                                    'domain':[-1,1], \
                                    'clipmode':'low', \
                                    'unique':False \
                                    })
print('param3', param3)