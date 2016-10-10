#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
local_path = os.path.abspath('./../')
print(local_path)
sys.path.append(local_path)

from pybush.project import new_project

my_project = new_project(name='My Python project')
my_device = my_project.new_device(name='My Python device', author='Pixel Stereo', version='0.1.0')
my_output = my_device.new_output(protocol='OSC')
my_node = my_device.new_child({'name':'NO NODE 1', 'tags':['uno', 'dos'], 'children':None, 'parameter':None})
print(my_output)
param1 = my_device.make_parameter()
my_project.write(local_path + '/examples/.tempfiles/my_project-from-save-file')
my_project.write(local_path + '/examples/export-test_project')