#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

sys.path.append(os.path.abspath('./../'))

import time
import liblo
import datetime
from pybush.constants import __dbug__
from time import sleep
from pybush.functions import m_bool, m_int, m_string, prop_list, prop_dict
from pybush import new_device, get_devices
from pybush.errors import BushTypeError, NoOutputError

from pybush.automation import RampGenerator, RandomGenerator

__dbug__ = 4

def announcement(test):
    print(' ')
    print('---TESTING ' + test + ' -----')
    print(' ')

my_device = new_device(name='My device', author='Pixel Stereo', version='0.1.0')
another_device = new_device(name='My device', author='Stereo Pixel', version='0.1.1')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
midi_output = my_device.new_output(protocol='MIDI')
#node_1 = my_device.new_child(name='node.1')
#node_2 = node_1.new_child(name='node.2', tags=['lol', 'lal'])
#param0 = my_device.new_parameter(name='punk one')
param2 = my_device.new_parameter({  'name':'node.1',
                                    'value':1,
                                    'datatype':'decimal',
                                    'domain':[0,11], \
                                    'clipmode':'both',
                                    'unique':True,
                                    'tags':['un', 'deux']
                                    })
#node_1.tags=['init', 'video']
print(param2)
param3 = my_device.new_parameter({  'name':'node.1/node.2',
                                    'value':-0.5, \
                                    'datatype':'decimal', \
                                    'domain':[-1,1], \
                                    'clipmode':'low', \
                                    'unique':False \
                                    })
parameter = my_device.new_parameter({'name':'/one/two/three/four/five/polo'})
# create two parameters with the same name must be raised
same = my_device.new_parameter({'name':'one/two/three/four/same'})
param3.ramp(2, 100)
sleep(0.2)
param3.random(2, 100)

# it is not possible for the moment to snap a device
"""snap_device = my_device.snap()
print('-----_______---')
print(snap_device)
print('-----_______---')"""
param2.value = 0
param2.ramp(1, 500)
param3.value = 1
param3.datatype = 'decimal'
param3.ramp(0, 500)
sleep(0.5)
param3.domain = [0.4, 0.6]
param3.random(destination=1, duration=700)
param2.random(1, 700)
print(param2.value)
param3.value = 0.5
sleep(0.7)
param2.ramp(0, 50)
param2.value = 1

node_1 = param2.parent
node_2 = param3.parent
node_3 = node_2.new_child(name="node.3")


class TestAll(unittest.TestCase):

    def test_a_snapshot(self):
        announcement('SNAPSHOT')
        snap_1 = param2.snap()
        print(snap_1.value)
        #print(1, param2.value)
        node_1.value = 212
        #print(3, param2.value)
        snap_2 = param2.snap()
        #node_1.recall(snap_1)
        #print(3, param2.value)
        #self.assertEqual(param2.value, 2)

    def test_device(self):
        announcement('DEVICE')
        self.assertEqual(isinstance(my_device.author, str), True)
        self.assertEqual(my_device.author, 'Pixel Stereo')
        self.assertEqual(isinstance(my_device.version, str), True)
        self.assertEqual(my_device.version, '0.1.0')
        self.assertEqual(type(my_device.name), str)
        self.assertEqual(my_device.name, 'My_device')
        self.assertEqual(len(get_devices()), 2)


    def test_nodes(self):
        announcement('NODES')
        xprt_node2 = node_2.export()
        self.assertEqual(isinstance(xprt_node2, dict), True)
        self.assertEqual(len(my_device.children), 2)
        self.assertEqual(len(node_1.children), 1)
        self.assertEqual(len(node_2.children), 1)
        #node_1.name = 'node 1 renamed'

    def test_device_export(self):
        announcement('EXPORT')
        xprt = my_device.export()
        self.assertEqual(isinstance(xprt, dict), True)
        xprt_name = xprt['author']
        self.assertEqual(xprt_name, 'Pixel Stereo')

    def test_prop_list(self):
        announcement('PROP_LIST')
        self.assertEqual(len(prop_dict(node_1).keys()), 5)
        self.assertEqual(len(prop_list(node_1)), 7)

    def test_parameter(self):
        announcement('PARAMETER')
        self.assertEqual(param2.__class__.__name__, 'Parameter')
        self.assertEqual(param2.value, 1)
        self.assertEqual(param2.unique, True)
        self.assertEqual(param2.datatype, 'decimal')
        self.assertEqual(param2.clipmode, 'both')
        self.assertEqual(param2.domain, [0, 11])

    def test_ramp(self):
        announcement('RAMP')
        a_random = RandomGenerator(param2, 0, 1, 1000, 10)
        for rand in a_random.random():
            self.assertEqual(rand > 0, True)
            self.assertEqual(rand < 11, True)
        a_ramp = RampGenerator(param3, 0.4, 1.6, 1000, 100)
        for step in a_ramp.ramp():
            self.assertEqual(step > 0.4, True)
            self.assertEqual(step < 1.7, True)
        #self.assertEqual(next(a_ramp), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_writing_files(self):
        announcement('WRTING / READING FILES')
        #self.assertEqual(node_1.parameter, param2)
        setattr(node_1, 'parameter', param2)
        write_path = os.path.abspath('./')
        write_path = write_path + '/'
        my_device.name = 'export-device.name attribute'
        device_write_path = write_path + 'export-test_device'
        self.assertEqual(my_device.write(device_write_path), True)
        self.assertEqual(my_device.write('/no/fake/BOGUS'), False)
        self.assertEqual(my_device.write(), False)
        filepath = os.path.abspath('export-test_device.bush')
        device = new_device()
        print(device.read(filepath))

    def test_modular_functions(self):
        announcement('MODULAR FUNCTIONS')
        b = 2
        self.assertEqual(isinstance(b, int), True)
        b = m_bool(b)
        self.assertEqual(isinstance(b, bool), True)
        b = 0
        self.assertEqual(isinstance(b, int), True)
        b = m_bool(b)
        self.assertEqual(isinstance(b, bool), True)
        i = 22.22
        self.assertEqual(isinstance(i, float), True)
        i = m_int(i)
        self.assertEqual(isinstance(i, int), True)
        i = [22.22]
        self.assertEqual(isinstance(i, list), True)
        i = m_int(i)
        self.assertEqual(isinstance(i, int), True)
        s = 2
        self.assertEqual(isinstance(s, int), True)
        s = m_string(s)
        self.assertEqual(isinstance(s, str), True)
        s = [2]
        self.assertEqual(isinstance(s, list), True)
        s = m_string(s)
        self.assertEqual(isinstance(s, str), True)
        parameter.value = 3.2
        parameter.datatype = 'decimal'
        parameter.tags = ['uno','dos']
        parameter.domain = [0,1]
        parameter.clipmode = 'both'
        parameter.unique = 1
        # here, we just assign the parameter as False
        self.assertEqual(same, same)
        self.assertEqual(parameter.value, 1)
        parameter.value = -2.2
        self.assertEqual(parameter.value, 0)
        self.assertEqual(parameter.raw, -2.2)
        self.assertEqual(isinstance(parameter.value, float), True)
        parameter.datatype = 'integer'
        self.assertEqual(isinstance(parameter.value, int), True)
        parameter.datatype = 'string'
        self.assertEqual(isinstance(parameter.value, str), True)
        parameter.datatype = None
        self.assertEqual(isinstance(parameter.value, float), True)

    def test_print(self):
        announcement('PRINT')
        print('----------------------------')
        print(my_device.name + " version " + my_device.version + " by " + my_device.author)
        #for key, val in param2.export().items():
        #    print('iterate', key, val)

    def test_address(self):
        announcement('ADDRESSES')
        self.assertEqual(my_device.address, 'My_device')
        self.assertEqual(node_1.address, 'My_device/node.1')
        self.assertEqual(node_2.address, 'My_device/node.1/node.2')
        self.assertEqual(node_3.address, 'My_device/node.1/node.2/node.3')
        self.assertEqual(param2.address, 'My_device/node.1')
        self.assertEqual(param3.address, 'My_device/node.1/node.2')

    def test_errors(self):
        announcement('RASING ERRORS')
        with self.assertRaises(BushTypeError) as cm:
            my_device.output = None
        the_exception = cm.exception
        self.assertEqual(the_exception.error_code, 1)

if __name__ == '__main__':
    unittest.main()
