#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('./../'))

from time import sleep
from pybush.project import new_project, projects

my_project = new_project(name='My Python project')
my_application = my_project.new_application(name='My Python application', author='Pixel Stereo', version='0.1.0')

another_application = my_project.new_application(name='My Other Python application', author='Stereo Pixel', version='0.1.1')
output = my_application.new_output(protocol='OSC', port='127.0.0.1:1234')
output = my_application.new_output(protocol='MIDI')
node_1 = my_application.new_child(name='node.1', tags=['init', 'video'])
node_2 = node_1.new_child(name='node .2', tags=['lol', 'lal'])
node_3 = node_2.new_child(name="node.3")
param1 = my_application.make_parameter()
param2 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'domain':[0,11], \
                                'clipmode':'both', 'repetitions':True})
param3 = node_2.make_parameter(value=-0.5, datatype='decimal', \
                                domain=[-1,1], clipmode='low', repetitions=False)

snap_param3 = param3.new_snapshot()
print(snap_param3)
snap_application = my_application.new_snapshot()
print('APPLCATION SNAPSHOT ', snap_application)
snap_project = my_project.new_snapshot()
print('PROJECT SNAPSHOT', snap_project)
print(my_application.export())
print(my_application.write())
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
param2.value = 1
print('ramp start')
my_ramp = param2.ramp(0, 1000)
sleep(0.2)
my_ramp.stop()
while my_ramp.is_alive():
	pass
print('ramping is over')
