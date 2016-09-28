#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.functions import prop_dict
from pybush.file import File
from pybush.constants import __dbug__, _file_extention


class Node(File):
    """Base Class for all item in the namespace"""
    def __init__(self, name, parent, service='node', tags=None, priority=None):
        super(Node, self).__init__(name, parent)
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self._service = service
        self._tags = tags
        self._priority = priority
        # initialise children nodes for this node
        self._children = []
        # initialise parameters for this node
        self._parameters = []

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags)

    def parameter_new(self, *args, **kwargs):
        """
        Create a Parameter in the current Node
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        for param in self._parameters:
            if param.name == args[0]:
                return False
        size = len(self._parameters)
        from pybush.paramter import Parameter
        self._parameters.append(Parameter(args[0], self))
        for key, value in kwargs.items():
            setattr(self._parameters[size], key, value)
        return self._parameters[size]

    def node_new(self, *args, **kwargs):
        """
        Create a new Node in its parent
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        for node in self._children:
            if node.name == args[0]:
                return False
        size = len(self._children)
        self._children.append(Node(args[0], self))
        for key, value in kwargs.items():
            setattr(self._children[size], key, value)
        return self._children[size]

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """ 
        return {self.name:prop_dict(self)}

    @property
    def parameters(self):
        """
        Return the list of the parameters registered to this node
        """
        return self._parameters

    @property
    def service(self):
        """
        Return the service of the node
        """
        return self.__class__.__name__

    @property
    def parent(self):
        """
        Return the parent of the node
        """
        print(self.name + ' comes from ' + self._parent.name)
        return self._parent.name

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

    # ----------- TAGS -------------
    @property
    def tags(self):
        """
        Current tags of the node
        """
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags
    @tags.deleter
    def tags(self):
        return False

    # ----------- PRIORITY -------------
    @property
    def priority(self):
        """
        Current priority of the node
        """
        return self._priority
    @priority.setter
    def priority(self, priority):
        self._priority = priority
    @priority.deleter
    def priority(self):
        return False
