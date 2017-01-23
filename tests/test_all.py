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
from pybush.errors import BushTypeError, NoOutputError
from pprint import pprint

__dbug__ = 4

my_project = new_project(name='My Python project')
my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')
node_1 = my_device.new_child(name='node.1')
node_1.parameter = {
                    'name':'node.1',
                    'value':1,
                    'datatype':'decimal',
                    'domain':[0,11],
                    'clipmode':'both',
                    'unique':True
                    }
snap = node_1.parameter.snap()
my_project.write('./')

another_project = new_project(name='Another Project')
lala = another_project.read('./My Python Project.bush')
print(lala)


class TestAll(unittest.TestCase):

    def test_node(self):
        self.assertEqual(my_device.children[0].__class__.__name__, 'Node')

    def test_parameter(self):
        self.assertEqual(my_device.children[0].parameter.__class__.__name__, 'Parameter')

    def test_snap(self):
        self.assertEqual(my_device.children[0].parameter.snapshots[0].__class__.__name__, 'Snapshot')

if __name__ == '__main__':
    unittest.main()
