#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export, fillin


filepath = os.path.abspath('export-test_device.bush')
devices = fillin(filepath)
print('----------------------')
print('----------------------')
for device in devices:
	#print(device.export())
	for child in device.children:
		print(child.export())
	#for key, val in device.export():
	#	print(key)
	#	print('------')
	#	print(val)
#print devices[0].children
#print(devices[0].export())
