#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.functions import prop_dict
from pybush.constants import __dbug__


class Node(object):
    """Base Class for all item in the namespace"""
    def __init__(self, name, tags=None, priority=None):
        # initialise attributes/properties of this node
        self._name = name
        self._tags = tags
        self._priority = priority
        # initialise children nodes for this node
        self._nodes = []
        # initialise parameters for this node
        self._parameters = []
        if __dbug__:
            print ("........... NODE %s Inited  ..........." %name)

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags})'
        return printer.format(name=self.name, priority=self.priority, tags=self.tags)

    """def __repr__(self):
        return str({self.name: prop_dict(self)})"""

    def parameter_new(self, *args, **kwargs):
        """
        Create a Parameter in the current Node
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        size = len(self._parameters)
        from pybush.leaf import Parameter
        self._parameters.append(Parameter(args[0]))
        for key, value in kwargs.items():
            setattr(self._parameters[size], key, value)
        return self._parameters[size]

    def node_new(self, *args, **kwargs):
        """
        Create a new Node in its parent
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        size = len(self._nodes)
        self._nodes.append(Node(args[0]))
        for key, value in kwargs.items():
            setattr(self._nodes[size], key, value)
        return self._nodes[size]
    
    def export(self):
        return {self.name:prop_dict(self)}

    @property
    def parameters(self):
        return self._parameters

    @property
    def nodes(self):
        """return the list of the nodes"""
        return self._nodes

    @property
    def name(self):
        "Current name of the node"
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @name.deleter
    def name(self):
        pass

    # ----------- TAGS -------------
    @property
    def tags(self):
        "Current tags of the node"
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags
    @tags.deleter
    def tags(self):
        pass

    # ----------- PRIORITY -------------
    @property
    def priority(self):
        "Current priority of the node"
        return self._priority
    @priority.setter
    def priority(self, priority):
        self._priority = priority
    @priority.deleter
    def priority(self):
        pass
