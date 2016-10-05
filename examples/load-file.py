#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.project import new_project


filepath = os.path.abspath('export-test_project.bush')
project = new_project()
project.read(filepath)
print('----------------------')
print('----------------------')
print(len(project.devices))
print(project.devices[0].children)
for device in project.devices:
	print(device.export())
	for child in device.children:
		print(child.export())
	#for key, val in device.export():
	#	print(key)
	#	print('------')
	#	print(val)
#print devices[0].children
#print(devices[0].export())
