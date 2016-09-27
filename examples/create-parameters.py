#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export

def headerprint(args):
	print('')
	print(args)
	print('-----------------------')
	
headerprint('create the device')
device = device_new('My Device')

headerprint('create two nodes')
node_1 = device.node_new('node.1')
node_2 = device.node_new('node.2')

headerprint('create a parameter for node.1')
param_1 = node_1.parameter_new('param.1', value=-1, datatype='decimal', tags=['uno','dos'], \
                                 priority=-1, domain=[0,1], clipmode='both', \
                                 repetitionsFilter=1)
headerprint('export to json file')
import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint
print('------------------ EXPORT NAMESPACE -------------------------------')
pprint(devices_export())