#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.constants import __dbug__
from pybush.functions import spacelessify


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
        It acts as a nick name.
        You can have several nodes with the same name
        Read-Only

        :Returns:String
        """
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    # ----------- DESCRIPTION -------------
    @property
    def description(self):
        """
        Description of this node
        You could here send a few words explainig this node.

        :Args:String
        :Returns:String
        """
        return str(self._description)
    @description.setter
    def description(self, description):
        self._description = description

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
            address = spacelessify(self.name)
            if self.__class__.__name__ is not 'Device':
                if self.parent:
                    parent_address = (get_address(self.parent))
                    if self.__class__.__name__ is 'Parameter':
                        address = parent_address
                    else:
                        address = parent_address + '/' + address
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
        """
        add a tag to this node
        """
        if tag in self._tags:
            if __dbug__ >= 3:
                print('already in')
        else:
            self._tags.append(tag)
    def del_tag(self, tag):
        """
        del a tag for this node
        """
        if tag in self._tags:
            self._tags.remove(tag)
        else:
            if __dbug__ >= 3:
                print('not in')
