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

headerprint('create a node')
node_1 = device.new_child('node.1')
node_1.tags = ['tag', 'for', 'node_1']

print(node_1)
node_1.make_parameter()
print(node_1)