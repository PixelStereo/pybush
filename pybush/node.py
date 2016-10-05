#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.functions import prop_dict
from pybush.constants import __dbug__, _file_extention
from pybush.node_abstract import NodeAbstract
from pybush.parameter import Parameter


class Node(NodeAbstract):
    """Base Class for all item in the namespace"""
    def __init__(self, name, parent, service='no', tags=None, priority=None, param=None, children=[]):
        super(Node, self).__init__(parent, service='no', tags=None, priority=None)
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority
        self._children = children
        self._parameter = param

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        nod = {}
        print(self)
        print('------- ------- EXPORTING ' + self.name)
        if self.parameter:
            param_export = self.parameter.export()
        else:
            param_export = self.parameter
        nod.update({'name':self.name, 'tags':self.tags, \
                                    'priority':self.priority, 'children':[], 'parameter':param_export})
        if self.children:
            for child in self.children:
                    nod['children'].append({'name':child.name, 'tags':child.tags, 'priority':child.priority, 'children':[]})
                    """for child1 in child.children:
                        nod[self.name]['children'][child.name]['children'].setdefault(child1.name, { 'name':child1.name, 'tags':child1.tags, \
                                                'priority':child1.priority, 'children':{}})
                        for child2 in child1.children:
                            nod[self.name]['children'][child.name]['children'][child1.name]['children'].setdefault(child2.name, { 'name':child2.name, 'tags':child2.tags, \
                                                'priority':child2.priority, 'children':{}})
                            for child3 in child2.children:
                                nod[self.name]['children'][child.name]['children'][child1.name]['children'][child2.name]['children'].setdefault(child3.name, { 'name':child3.name, 'tags':child3.tags, \
                                                'priority':child3.priority, 'children':{}})"""
        print('------- ------- END OF EXPORTING NODE ' + self.name)
        print('------- ------- VIEW ' + self.name)
        print(nod)
        print('------- ------- END OF VIEW ' + self.name)
        return nod
        
    @property
    def children(self):
        """
        Return the list of the children registered to this node

        :param path: valid filepath. Return True if valid, False otherwise.
        :type path: string
        """
        return self._children

    @property
    def parameter(self):
        """
        This is a parameter property
        Return the Parameter Object if it exists, return None otherwise
        Return the parameter dict otherwise
        """
        return self._parameter
    @parameter.setter
    def parameter(self, parameter_object):
        if self.parameter == None:
            self._parameter = Parameter(self)
        else:
            print('WHY DO YOU WANT TO CHANGE THE PARAMETER OBJECT OF THIS NODE ????', self.name)
        self._parameter = parameter_object

    def new_child(self, *args, **kwargs):
        """
        Create a new Node in its parent
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        children = self.children
        for child in children:
            if child.name == args[0]:
                return False
        size = len(self.children)
        self._children.append(Node(args[0], self))
        for key, value in kwargs.items():
            setattr(self._children[size], key, value)
        return self.children[size]

    def make_parameter(self):
        self._parameter = Parameter(self)
        return self._parameter
