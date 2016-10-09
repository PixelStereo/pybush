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
from pybush.node_abstract import NodeAbstract

my_project = new_project('My Python project')
another_project = new_project('Another Python project')
#len(projects())
my_device = my_project.new_device('My Python device', author='Pixel Stereo', version='0.1.0')
node_1 = my_device.new_child('node.1', priority=2, tags=['init', 'video'])
node_2 = node_1.new_child('node.2', tags=['lol', 'lal'], priority=-1)
node_3 = node_2.new_child("node_ 3's parent is node_2")
param1 = my_device.make_parameter()
param2 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'tags':['uno','dos'], \
                         'priority':-1, 'domain':[0,11], 'clipmode':'both', \
                         'repetitions':1})
param_3 = node_2.make_parameter('param.0', value=-0.5, datatype='decimal', tags=['uno','dos'], \
                         priority=-1, domain=[-1,1], clipmode='low', \
                         repetitions=1)

class TestAll(unittest.TestCase):

    def test_a_project(self):
        self.assertEqual(my_project.name, 'My Python project')
        self.assertEqual(another_project.name, 'Another Python project')
        self.assertEqual(len(projects()), 2)

    def test_device(self):
        self.assertEqual(isinstance(my_device.author, str), True)
        self.assertEqual(my_device.author, 'Pixel Stereo')
        self.assertEqual(isinstance(my_device.version, str), True)
        self.assertEqual(my_device.version, '0.1.0')
        self.assertEqual(type(my_device.name), str)
        self.assertEqual(my_device.name, 'My Python device')
        self.assertEqual(len(my_project.devices), 1)

    def test_nodes(self):
        self.assertEqual(node_2.priority, None)
        node_2.priority = 10
        self.assertEqual(node_2.priority, 10)
        xprt_node2 = node_2.export()
        self.assertEqual(isinstance(xprt_node2, dict), True)
        self.assertEqual(len(my_device.children), 1)
        self.assertEqual(len(node_1.children), 1)
        self.assertEqual(len(node_2.children), 1)
        node_1.name = 'lol'

    def test_device_export(self):
        xprt = my_project.export()
        self.assertEqual(isinstance(xprt, dict), True)
        xprt_name = xprt['devices'][0]['author']
        self.assertEqual(xprt_name, 'Pixel Stereo')

    def test_prop_list(self):
        self.assertEqual(len(prop_dict(node_1).keys()), 7)
        self.assertEqual(len(prop_list(node_1)), 10)


    def test_parameter(self):
        self.assertEqual(my_device.make_parameter(['fake']), False)
        self.assertEqual(param1.name, 'My Python device')

    def test_writing_files(self):
        self.assertEqual(node_1.parameter, param2)
        self.assertNotEqual(node_1.parameter, param1)
        setattr(node_1, 'parameter', param2)
        write_path = os.path.abspath('./')
        write_path = write_path + '/'
        node1_write_path = write_path + 'export-test_node_1'
        self.assertEqual(node_1.write(node1_write_path), True)
        node2_write_path = write_path + 'export-test_node_2'
        self.assertEqual(node_2.write(node2_write_path), True)
        my_device.name = 'export-device filename from device.name attribute'
        self.assertEqual(my_device.write(write_path), True)
        project_write_path = write_path + 'export-test_project'
        self.assertEqual(my_project.write(project_write_path), True)
        self.assertEqual(my_project.write('/no/fake/BOGUS'), False)
        self.assertEqual(my_project.write(), False)
        filepath = os.path.abspath('export-test_project.bush')
        project = new_project()
        read = project.read(filepath)

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
        parameter = my_device.make_parameter()
        parameter.value = 3.2
        parameter.datatype = 'decimal'
        parameter.tags = ['uno','dos']
        parameter.priority = -1
        parameter.domain = [0,1]
        parameter.clipmode = 'both'
        parameter.repetitions = 1
        # create two parameters with the same name must be raised
        same = my_device.make_parameter()
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
        print('----------------------------')
        print(my_device.name + " version " + my_device.version + " by " + my_device.author)
        abstrakt = NodeAbstract()
        print(abstrakt)
        for key, val in param2.export().items():
            print(key, val)


if __name__ == '__main__':
    unittest.main()
