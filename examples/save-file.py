print('PARENT')#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export

import pprint
pprint = pprint.PrettyPrinter(indent=2).pprint

def headerprint(args):
	print('')
	print(args)
	print('-----------------------')
	
headerprint('create the device')
device = device_new('My Device')

headerprint('create two nodes')
node_1 = device.new_node('node.1')
pprint(node_1.export())
node_2 = node_1.new_node('node.2')

headerprint('create a parameter for node.1')
param_1 = node_1.make_parameter()
param_1.value = -1
param_1.datatype = 'decimal'
param_1.tags = ['uno','dos']
param_1.priority = -1
param_1.domain = [0,1]
param_1.clipmode = 'both'
param_1.repetitions = 1
headerprint('create a parameter for node.2')
param_2 = node_2.make_parameter()
param_2.value = 2
param_2.datatype = 'decimal'
param_2.tags = ['uno','dos']
param_2.priority = -1
param_2.domain = [0,1]
param_2.clipmode = 'both'
param_2.repetitions=1
headerprint('create a root parameter')
param_0 = device.make_parameter()
param_0.value = -1
param_0.datatype = 'decimal'
param_0.tags = ['uno','dos']
param_0.priority = -1
param_0.domain = [0,1]
param_0.clipmode = 'both'
param_0.repetitions = 1

headerprint('export to json file')
print('------------------ EXPORT NODE 1 -------------------------------')
pprint(node_1.export())
print('------------------ END OF EXPORT NODE 1 -------------------------------')
print('------------------ EXPORT ALL DEVICES -------------------------------')
pprint(devices_export())
print('------------------ END OF ALL DEVICES -------------------------------')
print(device.write())
print(device.write('/Volumes/work/Users/reno/Documents/GITs/pybush/examples/export-test_device'))
print(node_1.write('/Volumes/work/Users/reno/Documents/GITs/pybush/examples/export-test_node_1'))
print(node_2.write('/Volumes/work/Users/reno/Documents/GITs/pybush/examples/export-test_node_2'))
