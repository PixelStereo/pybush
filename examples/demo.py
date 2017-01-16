#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('./../'))

from time import sleep
from pybush.project import new_project, projects

my_project = new_project(name='My Python project')
my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')

another_device = my_project.new_device(name='My Other device', author='Stereo Pixel', version='0.1.1')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
output = my_device.new_output(protocol='MIDI')
node_1 = my_device.new_child(name='node.1', tags=['init', 'video'])
node_2 = node_1.new_child(name='node .2', tags=['lol', 'lal'])
node_3 = node_2.new_child(name="node.3")
param1 = my_device.make_parameter()
param2 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'domain':[0,11], \
                                'clipmode':'both', 'repetitions':True})
param3 = node_2.make_parameter(value=-0.5, datatype='decimal', \
                                domain=[-1,1], clipmode='low', repetitions=False)

snap_param3 = param3.new_snapshot()
#print(snap_param3)
param3.clipmode = "both"
param3.domain = [-1, 1]
param3.datatype = "decimal"
param3.unique = True
param3.value = 0.5
snap2_param3 = param3.new_snapshot()
#print(snap2_param3)
param3.recall(snap_param3)
#print(param3)
param3.recall(snap2_param3)
#print(param3)
for snap in param3.snapshots:
	print(param3.snapshots.index(snap), snap)
snap_device = my_device.new_snapshot()
print('DEVICE SNAPSHOT ', snap_device)
snap_project = my_project.new_snapshot()
print('PROJECT SNAPSHOT', snap_project)
print(my_device.export())
print(my_device.write())
param2.value = 0
param2.ramp(1, 3000)
sleep(1.5)
param2.domain = [0.1, 0.4]
param2.random(0.1, 3000)
param3.value = 1
param3.datatype = 'decimal'
param3.ramp(0, 500)
sleep(0.5)
param3.domain = [0.4, 0.6]
param3.random(destination=1, duration=700)
param3.value = 0.7
param2.ramp(0, 500)
sleep(0.7)
param2.value = 1
print('ramp start')
my_ramp = param2.ramp(0, 1000)
sleep(0.5)
my_ramp.terminate()
while my_ramp.is_alive():
	pass
print('ramping is over')
