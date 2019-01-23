#! /usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from pybush import new_device

my_device = new_device(name='test device', author='Pixel Stereo', version='0.1.0')
osc_output = my_device.new_output(protocol='OSC', port='127.0.0.1:5000')
midi_output = my_device.new_output(protocol='MIDI', port='IAC 1')

my_int = my_device.add_param({
									'name':'int',
									'value':8,
									'tags':['int', 'no_dot'],
									'datatype':'integer',
									'domain':[1,35],
									'clipmode':'low',
									'unique':False})


my_float = my_device.add_param({
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
pprint(my_device.export())

# WAIT UNTIL CMD+C
try:
    print("Press CMD+C to exit")
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    oscServer.close()
    sys.exit(0)