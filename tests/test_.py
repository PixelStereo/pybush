#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
from time import sleep

sys.path.append(os.path.abspath('./../'))

import time
import liblo
import datetime
from pybush.constants import __dbug__
from pybush.functions import m_bool, m_int, m_string, prop_list, prop_dict
from pybush.device import device_new, get_devices_list, devices_export

 
class TestAll(unittest.TestCase):

    def test_device(self):
        my_device = device_new('My Python device', author='Pixel Stereo', version='0.1.0')
        author = my_device.author
        name = my_device.name
        version = my_device.version
        self.assertEqual(isinstance(author, str), True)
        self.assertEqual(author, 'Pixel Stereo')
        self.assertEqual(isinstance(version, str), True)
        self.assertEqual(version, '0.1.0')
        self.assertEqual(type(name), str)
        self.assertEqual(name, 'My Python device')
        another_device = device_new('Another Py device')
        self.assertEqual(len(get_devices_list()), 2)

    def test_nodes(self):
        my_device = get_devices_list()[0]
        node_1 = my_device.node_new('node.1', priority=2, tags=['init', 'video'])
        node_2 = my_device.node_new('node.2', tags=['lol', 'lal'], priority=-1)
        node_2_bis = node_2.node_new('node.2.bis')
        self.assertEqual(node_2.priority, -1)
        node_2.priority = 10
        self.assertEqual(node_2.priority, 10)
        xprt_node2 = node_2.export()
        self.assertEqual(isinstance(xprt_node2, dict), True)
        self.assertEqual(len(my_device.nodes), 3)
        self.assertEqual(len(node_1.nodes), 0)
        self.assertEqual(len(node_2.nodes), 1)
        print(node_1)
        node_1.name = 'lol'

    def test_device_export(self):
        device = get_devices_list()[0]
        node = device.node_new('node')
        xprt = devices_export()
        self.assertEqual(isinstance(xprt, dict), True)
        xprt_name = xprt['devices']['My Python device']['attributes']['author']
        self.assertEqual(xprt_name, 'Pixel Stereo')

    def test_prop_list(self):
        node_1 = get_devices_list()[0].nodes[0]
        self.assertEqual(len(prop_dict(node_1).keys()), 6)
        self.assertEqual(len(prop_list(node_1)), 6)

    def test_parameter(self):
        device = get_devices_list()[1]
        param1 = device.parameter_new('param.1', value=-1, datatype='decimal', tags=['uno','dos'], \
                                 priority=-1, range=[0,1], clipmode='both', \
                                 repetitions=1)
        self.assertEqual(param1.name, 'param.1')

    def test_modular_functions(self):
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
        zop = get_devices_list()[1]
        parameter = zop.parameter_new('parameter', value=3.2, datatype='decimal', tags=['uno','dos'], \
                                 priority=-1, domain=[0,1], clipmode='both', \
                                 repetitions=1)
        print(parameter)
        # create two parameters with the same name must be raised
        same = zop.parameter_new('parameter')
        # here, we just assign the parameter as False
        self.assertEqual(same, False)
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
        del parameter.domain
        del parameter.datatype
        del parameter.repetitions
        del parameter.clipmode
        del parameter.value
        del parameter.priority
        del parameter.tags
        del parameter.name

    def test_print(self):
        zdevice = get_devices_list()[0]
        #print(zdevice)
        del zdevice.author
        del zdevice.version
        print('----------------------------')
        print(zdevice.name + " version " + zdevice.version + " by " + zdevice.author)

if __name__ == '__main__':
    unittest.main()
