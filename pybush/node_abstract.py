#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.functions import prop_dict
from pybush.constants import __dbug__, _file_extention


class NodeAbstract(object):
    """
    Abstract Base Class for all item in the namespace
    Need to be subclassed
    """
    def __init__(self, name, parent, service='no', tags=None, priority=None, children=[]):
        super(NodeAbstract, self).__init__()
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority
        self._children = children

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        nod = {}
        print('exporting ----------' + self.name)
        nod.setdefault(self.name, { 'name':self.name, 'tags':self.tags, \
                                    'priority':self.priority, 'children':{}})
        if self.children:
            for child in self.children:
                if child.service == 'Parameter':
                    for k, v in child.export().items():
                        nod[self.name].setdefault(k, v)
                else:
                    nod[self.name]['children'].setdefault(child.name, {'IIIIII':1})
        return nod

    def reset(self):
        """
        Clear the content of the node
        """
        pass

    @property
    def service(self):
        """
        Return the service of the node
        """
        return self.__class__.__name__
    @service.setter
    def service(self, service):
        pass

    @property
    def parent(self):
        """
        Return the parent of the node
        """
        print(self.name + ' comes from ' + self._parent.name)
        return self._parent.name

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

    def new_node(self, *args, **kwargs):
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

    def new_param(self, *args, **kwargs):
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
        self._children.append(Parameter(args[0], self))
        for key, value in kwargs.items():
            setattr(self._children[size], key, value)
        return self.children[size]

    @property
    def children(self):
        """
        Return the list of the children registered to this node

        :param path: valid filepath. Return True if valid, False otherwise.
        :type path: string
        """
        return self._children
