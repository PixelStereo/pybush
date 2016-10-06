#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.project import new_project, projects


filepath = os.path.abspath('export-test_project.bush')
project = new_project()
print('---------')
print('---------')
print('---------')
read = project.read(filepath)
print('---------')
print('---------')
print('---------')
project = projects()[0]
device = project.devices[0]
print('---- HOW MANY CHILDREN FOR DEVICE -----')
for dev in device.children:
	print(dev.name)
node_1 = device.children[0]
print('---- HOW MANY CHILDREN FOR NODE 1 -----')
for child in node_1.children:
	print(child.name)
print('---- PARAMETER -----')
print(node_1.parameter)
#print(len(read.children))
#quit()

print('----------------------')
print('------- VIEW AS STRING __repr__ ')
print('----------------------')
print(project.devices[0])
print('----------------------')
print('------- VIEW AS DICT ')
print('----------------------')
for device in project.devices:
	print(device.export())
#print devices[0].children
#print(devices[0].export())
