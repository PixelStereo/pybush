#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('./../'))

from time import sleep
from pybush import new_device

my_device = new_device(name='millumin', author='Pixel Stereo', version='0.1.0')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
"""opacity = my_device.new_parameter({
									'name':'Layer/opacity',
									'value':0.,
									'tags':['millumin', 'video'],
									'datatype':'decimal',
									'domain':[0,1],
									'clipmode':'both',
									'unique':True})
"""

# TODO
# don't push value when creating parameter
# make it silent?
column = my_device.new_parameter({
									'name':'action/launchColumn',
									'value':1,
									'tags':['millumin', 'video'],
									'datatype':'integer',
									'domain':[22,35],
									'clipmode':'low',
									'unique':False})


sleep(0.1)
# just send a value
column.value = 0
sleep(0.05)
# make a ramp$
column.ramp(20, 2000)
quit()
sleep(1.1)
column.random(2, 1000)
sleep(1.1)
# with silent activated, value is internally update,
# but the value is not spread to the world
column.silent = True
column.value = 4
# send manually the value to the world
column.update()
