#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.constants import __dbug__
from pybush.functions import spacelessify
from pybush import is_string


class NodeAbstract(object):
    """
    Abstract Base Class for all item in the namespace
    Need to be subclassed
    """
    def __init__(self, name='Untitled abstract Node', description="I'm an abstract node", \
                    parent=None, tags=None):
        super(NodeAbstract, self).__init__()
        # initialise attributes/properties of this node
        self._name = name
        self._description = description
        self._parent = parent
        self._tags = tags

    def __repr__(self):
        printer = 'NodeAbstract (name:{name}, description:{description}, tags:{tags})'
        return printer.format(name=self.name, description=self.description, tags=self.tags)

    def reset(self):
        """
        Clear the content of the node
        """
        pass

    # ----------- NAME -------------
    @property
    def name(self):
        """
        Current name of the node
        """
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    # ----------- ADDRESS -------------
    @property
    def address(self):
        """
        Current name of the node
        """
        def get_address(self):
            """
            recursive function to get into parent's hierarchy
            """
            address = self.name
            if self.__class__.__name__ is not 'Device':
                if self.parent:
                    if self.__class__.__name__ is 'Parameter':
                        address = get_address(self.parent)
                    else:
                        address = get_address(self.parent) + '/' + address
            return address
        return get_address(self)
    @address.setter
    def address(self, address):
        if __dbug__:
            print('come back later for setting a new address for a node', address)
            print(self.address)

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
        return self._parent

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

    def add_tag(self, tag):
        if tag in self._tags:
            if debug >= 3:
                print('already in')
        else:
            self._tags.append(tag)
    def del_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)
        else:
            if debug >= 3:
                print('not in')
