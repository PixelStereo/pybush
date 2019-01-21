#! /usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from pybush import new_device

my_device = new_device(name='test device', author='Pixel Stereo', version='0.1.0')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:5000')

my_float = my_device.add_param({
									'name':'test/float',
									'value':0.2,
									'tags':['float', 'decimal'],
									'datatype':'float',
									'domain':[-1,1],
									'clipmode':'both',
									'unique':True})

my_float.value = 0
my_float.ramp(1, 100)