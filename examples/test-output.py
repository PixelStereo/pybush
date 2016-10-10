#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
local_path = os.path.abspath('./../')
print(local_path)
sys.path.append(local_path)

from pybush.functions import prop_dict
from pybush.project import new_project

my_project = new_project('My Python project')
my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
param1 = my_device.make_parameter()
osc = my_device.new_output('OSC')
print(osc)
for prop, value in prop_dict(osc).items():
	print(prop, value)
print('port : ' + osc.port)
my_project.write(local_path + '/examples/.tempfiles/my_project-from-save-file')