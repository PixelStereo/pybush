#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.constants import __dbug__

class NodeAbstract(object):
    """
    Abstract Base Class for all item in the namespace
    Need to be subclassed
    """
    def __init__(self, name=None, parent=None, service=None, tags=None, priority=None):
        super(NodeAbstract, self).__init__()
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority

    def __repr__(self):
        printer = 'NodeAbstract (priority:{priority}, tags:{tags})'
        return printer.format(priority=self.priority, tags=self.tags)

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
        address = self.name
        if self.parent:
            address = self.parent.name + address
            if self.parent.parent:
                address = self.parent.parent.name + address
                if self.parent.parent.parent:
                    address = self.parent.parent.parent.name + address
                    if self.parent.parent.parent.parent:
                        address = self.parent.parent.parent.parent.name + address
        return address
    @address.setter
    def address(self, address):
        print('come back later for setting a new address for a node', self.address)

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
