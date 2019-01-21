#! /usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from pybush import new_device

My_device = new_device(name='test device', author='Pixel Stereo', version='0.1.0')
output = My_device.new_output(protocol='OSC', port='127.0.0.1:5000')

my_int = My_device.add_param({
									'name':'int',
									'value':8,
									'tags':['int', 'no_dot'],
									'datatype':'integer',
									'domain':[1,35],
									'clipmode':'low',
									'unique':False})


my_float = My_device.add_param({
									'name':'float',
									'value':0.2,
									'tags':['float', 'decimal'],
									'datatype':'float',
									'domain':[-1,1],
									'clipmode':'both',
									'unique':True})

from pprint import pprint
pprint(my_int.export())
pprint(my_float.export())
pprint(My_device.export())

# WAIT UNTIL CMD+C
try:
    print("Press CMD+C to exit")
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    oscServer.close()
    sys.exit(0)