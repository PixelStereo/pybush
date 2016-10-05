#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export, fillin

import pprint
pprint = pprint.PrettyPrinter(indent=2).pprint

filepath = os.path.abspath('export-test_device.bush')
devices = fillin(filepath)
#print len(devices)
#print devices[0].children
print(devices[0].export())
