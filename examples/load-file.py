#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

lib_path = os.path.abspath('./../')
sys.path.append(lib_path)
import pybush
from pybush.device import device_new, get_devices_list, devices_export
from pybush.file import File


filepath = os.path.abspath('export-test_device.bush')
file = File('file2load', 'no-parent')
data = file.read(filepath)
if data:
    print('DATA', data)
    
else:
    print('failed to load file')