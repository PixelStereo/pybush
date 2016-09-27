#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)

#import py
from pybush.device import device_new, get_devices_list

def headerprint(args):
	print ('---------------- ' + str(args) + ' ----------------')
	
# create the device
my_device = device_new('test_App',author='Pixel Stereo',version='0.0.1',project='my first application')

# create two nodes
node_1 = my_device.node_new('node.1')
node_2 = my_device.node_new('node.2')
node_3 = node_2.node_new('node.3')

# create a few parameters for app
param_0 = my_device.parameter_new('param.0',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)
# create a few parameters for node_1 and node_2
param_1 = node_1.parameter_new('param.1',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)
param_2 = node_1.parameter_new('param.2',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)
param_3 = node_2.parameter_new('param.3',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)
param_4 = node_2.parameter_new('param.4',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)
param_5 = node_3.parameter_new('param.5',value=-1,datatype='decimal',tags=['uno','dos'],priority=-1,rangeBounds=[0,1],rangeClipmode='both',repetitionsFilter=1)


def get_app_attr(app):
	attr_list = []
	for attr in dir(app):
		if not attr.startswith('__'):
			if not attr.startswith('_'):
				if not attr == 'instances':
					if not attr == 'name':
						attr_list.append(attr)
	return attr_list


headerprint('Application attributes')
for attr in get_app_attr(my_device):
	print (attr + ' : ' + str(getattr(my_device, attr)))


headerprint('Namespace Explorer')
print ('my_device has ' + str(len(my_device.nodes)) + ' nodes')

for child in my_device.nodes:
	if child.nodes:
		print(child.name + ' has children : ' + str(child.nodes))
	else:
		print(child.name + ' has no child')

print('----------------------------------------')
print('----------------------------------------')
for pop in vars(my_device):
	print pop
