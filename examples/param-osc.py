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
# create two nodes
node_1 = my_device.new_child('node.1')
node_2 = node_1.new_child('node.2')

# create a few parameters for node_1 and node_2
param_1 = node_1.make_parameter('param.1',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)
param_2 = node_2.make_parameter('param.2',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,domain=[0,1],clipmode='both',repetitions=1)

param_1.value = 12
param_2.value = 21

print('parent of param_1 is ' + param_1.parent.name)
print('parent of node_1 is ' + param_1.parent.parent.name + ' / ' + param_1.parent.parent.__class__.__name__)
print('parent of param_2 is ' + param_2.parent.name)
print('parent of node_2 is ' + param_2.parent.parent.name + ' / ' + param_2.parent.parent.__class__.__name__)