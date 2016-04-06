#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)

import pybush
from pybush.node import Node
from pybush.leaf import Parameter
from pybush.functions import prop_list
from pybush.application import application_new, applications, applications_export

import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint

# create an application
my_app = application_new('My Python App', author='Renaud Rubiano', version='0.1.0')
# create another application
another_app = application_new('Another Py App')
# create a few nodes
node_1 = my_app.node_new('node.1', priority=2, tags=['init','video'])
node_2 = my_app.node_new('node.2', tags=['lol', 'lal'], priority='-1')
node_3 = another_app.node_new('node.1', tags=['pol', 'pal'], priority='-11')
node_2_bis = node_2.node_new('node.2.bis')
msg = ('BEFORE tags were {tags} and priority was {priority}')
print(msg.format(priority=node_2.priority, tags=node_2.tags))
node_2.priority = 10
node_2.tags = ['toto', 'tata']
msg = ('AFTER tags are {tags} and priority is {priority}')
print(msg.format(priority=node_2.priority, tags=node_2.tags))

pprint(node_2.export())

for app in applications():
	print(app)
	for node in app.nodes:
		print('    ' + str(node))
the_class = app
#print('------------------ PROPERTIES OF AN APPLICATION-------------------------------')
#print prop_list(my_app)
#print('------------------ PROPERTIES OF A node -------------------------------')
#print prop_list(node_1)
print('------------------ EXPORT NAMESPACE -------------------------------')
pprint(applications_export())
