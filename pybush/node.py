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
    def __init__(self, name, parent, service='no', tags=None, priority=None, param=None):
        super(Node, self).__init__(parent, service='no', tags=None, priority=None)
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority
        self._parameter = param
        self._children = []

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags}, children:{children})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags, children=self.children)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        if self.parameter:
            param = self.parameter.export()
        else:
            param = None
        filiation = []
        if self.children:
            for child in self.children:
                filiation.append(child.export())
        return {'name':self.name, 'tags':self.tags, 'priority':self.priority, \
                'children':filiation, 'parameter':param}
        
    # ----------- children -------------
    @property
    def children(self):
        """
        Return the list of the children registered to this node
        """
        return self._children

    # ----------- NAME -------------
    @property
    def name(self):
        """
        Current name of the node
        """
        return self._name
    @name.setter
    def name(self, name):
        print('a name connot be changed for a node, or we might look if it already exists')
        return False
        #self._name = name
    @name.deleter
    def name(self):
        return False

    # ----------- PARAMETER -------------
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

    # ----------- MAKE_PARAMETER METHOD -------------
    def make_parameter(self):
        """
        Call this method to attach a parameter to this node
        """
        self._parameter = Parameter(self)
        return self._parameter

  # ----------- NEW CHILD METHOD -------------
    def new_child(self, *args, **kwargs):
        """
        Create a new Node in its parent
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        print('')
        print('')
        print(args[0], self)
        print('')
        print('')
        the_new_child = Node(args[0], self)
        self._children.append(the_new_child)
        return the_new_child
