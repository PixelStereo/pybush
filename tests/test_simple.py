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
from pybush.errors import BushTypeError, NoOutputError
from pybush.controler import Controler

__dbug__ = 4
my_project = new_project(name='My Python project')
my_device = my_project.new_device(name='My device', author='Pixel Stereo', version='0.1.0')
output = my_device.new_output(protocol='OSC', port='127.0.0.1:1234')
node_1 = my_device.new_child(name='node.1', tags=['init', 'video'])
param2 = node_1.make_parameter({'value':1, 'datatype':'decimal', 'domain':[0,11], \
                                'clipmode':'both', 'unique':True})

class TestAll(unittest.TestCase):

    def test_a_snapshot(self):
        snap_1 = param2.new_snapshot()
        print('THE SNAP 1 VALUE', snap_1.value)
        print('THE SNAP 1 DOMAIN', snap_1.domain)
        param2.value = 'popo'
        param2.domain = ['toto', 'tata']
        param2.datatype = 'string'
        param2.unique = False
        param2.clipmode = None
        #print(2, param2.value)
        #print('----------')
        #print('----------')
        #print(snap_1.export())
        #print('----------')
        #print('----------')
        snap_2 = param2.new_snapshot()
        print('THE SNAP 2 VALUE', snap_2.value)
        print('THE SNAP 2 DOMAIN', snap_2.domain)
        #print('THE SNAP 2', snap_2)
        #print(3)
        #print(snap_1.export())
        param2.recall(snap_1)
        print('THE RECALL 1 VALUE', param2.value)
        print('THE RECALL 1 DOMAIN', param2.domain)
        node_1.write('./')
        param2.recall(snap_1)
        print('THE RECALL 1 VALUE', param2.value)
        print('THE RECALL 1 DOMAIN', param2.domain)
        node_1.write('./')
        print(snap_1.write('./snap'))
        print(snap_2.write('./snap2'))
        print(my_project.write('./'))
        #print(my_project.export())
        print(my_project.reset())
        #print(my_project.export())
        toto = new_project(name='loading test')
        toto.load('./My Python project.bush')
        print('ALLEZ')
        print(toto.write('./My imported project'))
        #print(3, param2.value)
        #self.assertEqual(param2.value, 2)

if __name__ == '__main__':
    unittest.main()
