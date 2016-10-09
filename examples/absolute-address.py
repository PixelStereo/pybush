#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)

#import py
from pybush.project import new_project

def headerprint(args):
	print ('---------------- ' + str(args) + ' ----------------')
	
# create the project
my_project = new_project('project_test')

# create the device
my_device = my_project.new_device('device_test',author='Pixel Stereo',version='0.0.1',project='my first device')

# create three nodes
node_1 = my_device.new_child('node.1')
print('Exporting ' + my_device.name)
node_2 = my_device.new_child('node.2')
print(node_2.write('/Volumes/worK/Users/reno/Desktop/node_2'))
node_3 = node_2.new_child('node.3')
print(node_3.write('/Volumes/worK/Users/reno/Desktop/node_3'))

# create a few parameters for app
param_0 = my_device.make_parameter('param.0',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)
print(param_0.write('/Volumes/worK/Users/reno/Desktop/param_0'))

# create a few parameters for node_1, node_2 and node_3
param_1 = node_1.make_parameter('param.1',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)
param_2 = node_2.make_parameter('param.3',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)
param_3 = node_3.make_parameter('param.5',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)

param_1.value = 12
print(my_project.name)
print(my_project.address)
print(my_device.name)
print(my_device.address)
print(node_1.name)
print(node_1.address)
print(node_2.name)
print(node_2.address)
print(node_3.name)
print(node_3.address)
print(param_1.name)
print(param_1.address)
print(param_2.name)
print(param_2.address)
print(param_3.name)
print(param_3.address)
