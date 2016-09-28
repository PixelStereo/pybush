print('PARENT')#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export

import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint

def headerprint(args):
	print('')
	print(args)
	print('-----------------------')
	
headerprint('create the device')
device = device_new('My Device')

headerprint('create two nodes')
node_1 = device.node_new('node.1')
pprint(node_1.export())
node_2 = node_1.node_new('node.2')

headerprint('create a parameter for node.1')
param_1 = node_1.parameter_new('param.1', value=-1, datatype='decimal', tags=['uno','dos'], \
                                 priority=-1, domain=[0,1], clipmode='both', \
                                 repetitionsFilter=1)
headerprint('create a root parameter')
param_1 = device.parameter_new('param.0', value=-1, datatype='decimal', tags=['uno','dos'], \
                                 priority=-1, domain=[0,1], clipmode='both', \
                                 repetitionsFilter=1)

headerprint('export to json file')
print('------------------ EXPORT NAMESPACE -------------------------------')
pprint(node_1.export())
quit()
pprint(devices_export())
print(device.write())
print(device.write('/Volumes/work/Users/reno/Desktop/export-test_device'))
print(node_1.write('/Volumes/work/Users/reno/Desktop/export-test_node_1'))
print(node_2.write('/Volumes/work/Users/reno/Desktop/export-test_node_2'))
print(param_1.write('/Volumes/work/Users/reno/Desktop/export-test_param_1'))