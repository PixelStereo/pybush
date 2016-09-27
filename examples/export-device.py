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
headerprint('list device, nodes and parameters')
for device in get_devices_list():
    print('    ' +  str(device))
    for node in device.nodes:
        print('        ' +  str(node))
        for parameter in node.parameters:
            print('            ' +  str(parameter))


headerprint('try clipmode function')
print ('domain is : ' , param_1.domain)
print ('raw value is ' , param_1.raw)
print ('clipmode is : ' , param_1.clipmode)
print ('value is : ' , param_1.value)
param_1.clipmode = 'low'
print ('raw value is ' , param_1.raw)
print ('clipmode is : ' , param_1.clipmode)
print ('value is : ' , param_1.value)
param_1.value = 2
param_1.clipmode = 'high'
print ('raw value is ' , param_1.raw)
print ('clipmode is : ' , param_1.clipmode)
print ('value is : ' , param_1.value)
param_1.clipmode = 'both'
print ('raw value is ' , param_1.raw)
print ('clipmode is : ' , param_1.clipmode)
print ('value is : ' , param_1.value)

headerprint('repetitions')
print (param_1.repetitions)
param_1.repetitions = 0
print (param_1.repetitions)

headerprint('try priority function')
print (param_1.priority)
param_1.priority = 0
print (param_1.priority)

headerprint('tags')
print (param_1.tags)
param_1.tags = ['ein','zwei']
print (param_1.tags)

headerprint('name')
param_1.name = 22
print (param_1.name , type(param_1.name))
param_1.name = 'zobi'
print (param_1.name , type(param_1.name))

headerprint('datatype')
print (param_1.datatype)
param_1.datatype = 'integer'
print (param_1.datatype)

headerprint('set value and rangeClipmode')
param_1.value = 999.99
param_1.rangeClipmode = [0,1000]
print ('raw value is : ' , param_1.raw , 'and clipmode is : ' , param_1.clipmode)
print ('datatype is : ' , param_1.datatype , 'and value is so : ' , type(param_1.value) , param_1.value)
param_1.datatype = 'decimal'
print ('datatype is : ' , param_1.datatype , 'and value is so : ' , type(param_1.value) , param_1.value)


import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint
print('------------------ EXPORT NAMESPACE -------------------------------')
pprint(devices_export())