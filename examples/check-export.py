#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.project import new_project

import pprint
pprint = pprint.PrettyPrinter(indent=2).pprint

def headerprint(args):
	print('')
	print(args)
	print('-----------------------')
	
headerprint('create a project')
project = new_project('My Project')
pprint(project.export())

headerprint('create a device')
device = project.new_device('My Device')
pprint(device.export())

output = device.new_output(name='My Output', protocol='OSC')
pprint(output.export())

headerprint('create a node')
node_1 = device.new_child('node.1')
node_1.tags = ['tag', 'for', 'node_1']

pprint(node_1.export())

headerprint('THE PROJECT')
#pprint(project.export())

headerprint('create another node')
node_2 = node_1.new_child('node.2')

headerprint('create a parameter for node.1')
param_1 = node_1.make_parameter()
print(param_1)
param_1.value = -1
param_1.datatype = 'decimal'
param_1.tags = ['one','two']
param_1.domain = [0,1]
param_1.clipmode = 'both'
param_1.repetitions = 1

headerprint('THE PARAMETER')
print(node_1.parameter is param_1)
print(node_1.parameter.export())

headerprint('create a parameter for node.2')
param_2 = node_2.make_parameter()
param_2.value = 2
param_2.datatype = 'integer'
param_2.tags = ['uno','dos']
param_2.domain = [0,100]
param_2.clipmode = 'low'
param_2.repetitions=1

headerprint('THE OTHER PARAMETER')
print(node_2.parameter is param_2)
print(node_2.parameter.export())

headerprint('create a root parameter')
param_0 = device.make_parameter()
param_0.value = -1
param_0.datatype = 'decimal'
param_0.tags = ['uno','dos']
param_0.domain = [0,1]
param_0.clipmode = 'both'
param_0.repetitions = 1

headerprint('export to json file')
print('------------------ EXPORT NODE 1 -------------------------------')
pprint(node_1.export())
print('------------------ END OF EXPORT NODE 1 -------------------------------')
print('------------------ EXPORT A PROJECT -------------------------------')
pprint(project.export())
print('------------------ END OF A PROJECT -------------------------------')

