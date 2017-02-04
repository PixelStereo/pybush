#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('./../'))

from time import sleep
from pybush import new_device

my_device = new_device(name='millumin', author='Pixel Stereo', version='0.1.0')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:5000')

column = my_device.new_parameter({
									'name':'action/launchColumn',
									'value':1,
									'tags':['millumin', 'video'],
									'datatype':'integer',
									'domain':[1,35],
									'clipmode':'low',
									'unique':False})

state = column.make_state()
column.value = 12
state = column.make_state()
print('----')
print(column.states[0])

opacity = my_device.new_parameter({
									'name':'test/opacity',
									'value':0.,
									'tags':['millumin', 'video'],
									'datatype':'decimal',
									'domain':[0,1],
									'clipmode':'both',
									'unique':True})

from pprint import pprint
pprint(column.export())
pprint(my_device.export())

