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
from pybush.project import new_project, projects

 
class TestAll(unittest.TestCase):

    def test_a_project(self):
        my_project = new_project('My Python project')
        self.assertEqual(my_project.name, 'My Python project')
        another_project = new_project('Another Python project')
        self.assertEqual(another_project.name, 'Another Python project')
        self.assertEqual(len(projects()), 2)

    def test_device(self):
        my_project = new_project('My Python project')
        my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        author = my_device.author
        name = my_device.name
        version = my_device.version
        self.assertEqual(isinstance(author, str), True)
        self.assertEqual(author, 'Pixel Stereo')
        self.assertEqual(isinstance(version, str), True)
        self.assertEqual(version, '0.1.0')
        self.assertEqual(type(name), str)
        self.assertEqual(name, 'My Python device')
        another_device = my_project.new_device('Another Py device')
        self.assertEqual(len(my_project.devices), 2)

    def test_nodes(self):
        my_project = new_project('My Python project')
        my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        node_1 = my_device.new_child('node.1', priority=2, tags=['init', 'video'])
        node_2 = my_device.new_child('node.2', tags=['lol', 'lal'], priority=-1)
        node_2_bis = node_2.new_child('node.2.bis')
        self.assertEqual(node_2.priority, None)
        node_2.priority = 10
        self.assertEqual(node_2.priority, 10)
        xprt_node2 = node_2.export()
        self.assertEqual(isinstance(xprt_node2, dict), True)
        self.assertEqual(len(my_device.children), 2)
        self.assertEqual(len(node_1.children), 0)
        self.assertEqual(len(node_2.children), 1)
        node_1.name = 'lol'

    def test_device_export(self):
        my_project = new_project('My Python project')
        my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        node_1 = my_device.new_child('node.1', priority=2, tags=['init', 'video'])
        node_2 = my_device.new_child('node.2', tags=['lol', 'lal'], priority=-1)
        node_2_bis = node_2.new_child('node.2.bis')
        node = my_device.new_child('node')
        xprt = my_project.export()
        self.assertEqual(isinstance(xprt, dict), True)
        xprt_name = xprt['devices'][0]['author']
        self.assertEqual(xprt_name, 'Pixel Stereo')

    def test_prop_list(self):
        my_project = new_project('My Python project')
        my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        node_1 = my_device.new_child('node.1', priority=2, tags=['init', 'video'])
        self.assertEqual(len(prop_dict(node_1).keys()), 5)
        self.assertEqual(len(prop_list(node_1)), 7)

    def test_parameter(self):
        my_project = new_project('My Python project')
        my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        param1 = my_device.make_parameter()
        self.assertEqual(param1.name, 'My Python device')

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
        my_project = new_project('My Python project')
        zop = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        parameter = zop.make_parameter()
        parameter.value = 3.2
        parameter.datatype = 'decimal'
        parameter.tags = ['uno','dos']
        parameter.priority = -1
        parameter.domain = [0,1]
        parameter.clipmode = 'both'
        parameter.repetitions = 1
        print(parameter)
        # create two parameters with the same name must be raised
        same = zop.make_parameter()
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
        my_project = new_project('My Python project')
        zdevice = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
        #print(zdevice)
        del zdevice.author
        del zdevice.version
        print('----------------------------')
        print(zdevice.name + " version " + zdevice.version + " by " + zdevice.author)


if __name__ == '__main__':
    unittest.main()
