#! /usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from pybush import new_device

my_device = new_device(name='test device', author='Pixel Stereo', version='0.1.0')
my_device.new_output(protocol='OSC', port='127.0.0.1:1234')


my_int = my_device.add_param({
									'name':'int',
									'value':8,
									'tags':['int', 'no_dot'],
									'datatype':'integer',
									'domain':[1,35],
									'clipmode':'low',
									'unique':False})

my_device.new_input(protocol='OSC', port=1235)

try:
    print("Press CMD+C to exit")
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    sys.exit(0)