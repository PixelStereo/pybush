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
from pybush.project import new_project, projects
from pybush.node_abstract import NodeAbstract

__dbug__ = 4
my_project = new_project(name='My Python project')

another_project = new_project('Another Python project')
#len(projects())
my_application = my_project.new_application(name='My Python application', author='Pixel Stereo', version='0.1.0')
another_application = my_project.new_application(name='My Other Python application', author='Stereo Pixel', version='0.1.1')
output = my_application.new_output(protocol='OSC', port='127.0.0.1:1234')
output = my_application.new_output(protocol='MIDI')
node_1 = my_application.new_child(name='node.1', tags=['init', 'video'])
node_2 = node_1.new_child(name='node .2', tags=['lol', 'lal'])
node_3 = node_2.new_child(name="node.3")
param1 = my_application.make_parameter()
param2 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'domain':[0,11], \
                                'clipmode':'both', 'repetitions':True})
param3 = node_2.make_parameter(value=-0.5, datatype='decimal', \
                                domain=[-1,1], clipmode='low', repetitions=False)
snap_application = my_application.new_snapshot()
snap_project = my_project.new_snapshot()
print(snap_application)
print(snap_project)
print(my_application.export())
print(my_application.write())
param2.value = 0
param2.ramp(1, 500)
param3.value = 1
param3.datatype = 'decimal'
param3.ramp(0, 500)
sleep(0.5)
param3.domain = [0.4, 0.6]
param3.random(destination=1, duration=700)
param3.value = 0.5
param2.ramp(0, 500)
sleep(0.7)
param2.value = 1


class TestAll(unittest.TestCase):

    def test_a_snapshot(self):
        snap_1 = node_1.new_snapshot()
        node_1.parameter.value = 2
        snap_2 = node_1.new_snapshot()
        node_1.recall(snap_1)
        self.assertEqual(node_1.parameter.value, 1)

    def test_a_project(self):
        self.assertEqual(my_project.name, 'My Python project')
        self.assertEqual(another_project.name, 'Another Python project')
        self.assertEqual(len(projects()), 2)

    def test_application(self):
        self.assertEqual(isinstance(my_application.author, str), True)
        self.assertEqual(my_application.author, 'Pixel Stereo')
        self.assertEqual(isinstance(my_application.version, str), True)
        self.assertEqual(my_application.version, '0.1.0')
        self.assertEqual(type(my_application.name), str)
        self.assertEqual(my_application.name, 'My Python application')
        self.assertEqual(len(my_project.applications), 2)


    def test_nodes(self):
        xprt_node2 = node_2.export()
        self.assertEqual(isinstance(xprt_node2, dict), True)
        self.assertEqual(len(my_application.children), 1)
        self.assertEqual(len(node_1.children), 1)
        self.assertEqual(len(node_2.children), 1)
        node_1.name = 'node 1 namee'

    def test_application_export(self):
        xprt = my_project.export()
        self.assertEqual(isinstance(xprt, dict), True)
        xprt_name = xprt['applications'][0]['author']
        self.assertEqual(xprt_name, 'Pixel Stereo')

    def test_prop_list(self):
        self.assertEqual(len(prop_dict(node_1).keys()), 8)
        self.assertEqual(len(prop_list(node_1)), 11)


    def test_parameter(self):
        self.assertEqual(my_application.make_parameter(['fake']), False)

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
        my_application.name = 'export-application filename from application.name attribute'
        self.assertEqual(my_application.write(write_path), True)
        project_write_path = write_path + 'export-test_project'
        self.assertEqual(my_project.write(project_write_path), True)
        self.assertEqual(my_project.write('/no/fake/BOGUS'), False)
        self.assertEqual(my_project.write(), False)
        filepath = os.path.abspath('export-test_project.bush')
        project = new_project()
        read = project.load(filepath)

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
        parameter = my_application.make_parameter()
        parameter.value = 3.2
        parameter.datatype = 'decimal'
        parameter.tags = ['uno','dos']
        parameter.domain = [0,1]
        parameter.clipmode = 'both'
        parameter.repetitions = 1
        # create two parameters with the same name must be raised
        same = my_application.make_parameter()
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
        print(my_application.name + " version " + my_application.version + " by " + my_application.author)
        for key, val in param2.export().items():
            print(key, val)

    def test_abstract_node(self):
        abstrakt = NodeAbstract(name='Untitled abstract Node')
        self.assertEqual(abstrakt.name, 'Untitled abstract Node')
        abstrakt_2 = NodeAbstract(name='toto')
        self.assertEqual(abstrakt_2.name, 'toto')
        print(abstrakt)

    def test_address(self):
        self.assertEqual(my_application.address, 'My_Python_application')
        self.assertEqual(node_1.address, 'My_Python_application/node.1')
        self.assertEqual(node_2.address, 'My_Python_application/node.1/node_.2')
        self.assertEqual(node_3.address, 'My_Python_application/node.1/node_.2/node.3')
        self.assertEqual(param1.address, 'My_Python_application')
        self.assertEqual(param2.address, 'My_Python_application/node.1')
        self.assertEqual(param3.address, 'My_Python_application/node.1/node_.2')

if __name__ == '__main__':
    unittest.main()
