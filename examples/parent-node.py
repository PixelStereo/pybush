print('PARENT')#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.project import new_project

def headerprint(args):
	print('')
	print(args)
	print('-----------------------')
	
headerprint('create the project')
project = new_project('My Project')

headerprint('create the device')
device = project.new_device('My Device')

headerprint('create two nodes')
node_1 = device.new_child('node.1')
node_2 = node_1.new_child('node.2')

headerprint('create a parameter for node.1')
# you can do it with a dictionary
param_1 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'tags':['uno','dos'], \
                                 'domain':[0,11], 'clipmode':'both', \
                                 'repetitions':1})
headerprint('create a root parameter')
# or just with all the args with keywords
param_0 = device.make_parameter('param.0', value=-0.5, datatype='decimal', tags=['uno','dos'], \
                                 domain=[-1,1], clipmode='low', \
                                 repetitions=1)
headerprint('create a param parameter')
param_2 = node_2.make_parameter('param.2', value=20, datatype='integer', tags=['uno','dos'], \
                                 domain=[0,200], clipmode='high', \
                                 repetitions=0)
headerprint('----- Print parents ------')
import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint

print(device.children)

for child in device.children:
	headerprint('------- OWNED BY A NODE --------')
	print(child.name + ' has for parent ' + child.parent)
	print(child.parameter)
	for child in child.children:
		headerprint('------- PARAMETERS OWNED BY A NODE --------')
		print(child.name + ' has for parent ' + child.parent)
		print(child.parameter)