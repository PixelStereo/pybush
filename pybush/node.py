#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Node Class
The Node is based on the Basic class
It is the base class of all items in a namespace.
Device and Value are based on the Node Class
it
"""
from pybush.constants import __dbug__
from pybush.functions import spacelessify
from pybush.basic import Basic
from pybush.functions import set_attributes


class Node(Basic):
    """
    Base Class for all item in the namespace.
    It offers a way to have information / notification / functions
    about the namespace hierarchy
    It inherits from Basic Class. It adds name, description and tags functions.
    That export/import json files for any Node with all its chidren
    """
    def __init__(self, **kwargs):
        super(Node, self).__init__()
        # initialise attributes/properties of this node
        self._address = None
        self._parameter = None
        self._children = None
        # kwargs setup attributes
        set_attributes(self, kwargs)

    def post_print(self, printer):
        printer = 'Node' + printer
        if self.children:
            printer = printer + ' - children :  ' + str(len(self.children))
        if self.address:
            printer = printer + ' - address :  ' + self.address
        if self.parameter:
            val = str(self.parameter.value)
            printer = printer + ' - parameter value is : ' + val
        return printer

    @property
    def parameter(self):
        """
        parameter of the node
        """
        return self._parameter
    @parameter.setter
    def parameter(self, parameter):
        if parameter.__class__.__name__ == 'Parameter':
            self._parameter = parameter
            return True
        elif parameter.__class__.__name__ == 'dict':
            self._parameter = self.get_device().add_param(parameter)
            return bool(self._parameter)
        else:
            if __dbug__:
                print('ERROR 876 : this is not a Value instance, this is a ' + parameter.__class__.__name__)
            return False

    def get_device(self):
        """
        get the root device of this node
        """
        asker = self
        def get_parent(asker):
            """
            get the parent of the current node
            """
            print(asker)
            asker = asker.parent
            return asker
        while asker.service != 'Device':
            asker = get_parent(asker)
        return asker

    @property
    def children(self):
        """
        Return the list of the children registered to this node
        """
        if self._children:
            return self._children
        else:
            return None

    def new_child(self, dict_import=None, name=None, description=None, tags=None, children=None):
        """
        Create a new Node in its parent

        You can
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        def append_child(new_child):
            """
            append the child to the children list of this instance
            """
            if not self.children:
                self._children = [new_child]
            else:
                self._children.append(new_child)
        if not isinstance(dict_import, dict):
            dict_import = {'name':name, 'description':description, 'tags':tags}
        if isinstance(dict_import, dict):
            if 'name' in dict_import.keys():
                # check that the name doesn't already exists
                if self.children:
                    for child in self.children:
                        if isinstance(child, list):
                            child = child[0]
                        if isinstance(child, Node):
                            if dict_import['name'] == child.name:
                                # return the existing child if it already exists
                                return child
                # we import a python dict to create the child
                # be careful about children and parameter
                # which needs to instanciate Classes Node and Value
                the_new_child = Node(parent=self, **dict_import)
                # Append this child in the self.children list
                append_child(the_new_child)
                # maybe the new_child contains children itself?
                if 'children' in dict_import.keys():
                    if len(dict_import['children']) > 0:
                        for little_child in dict_import['children']:
                            # create a new child for each of the new_child.children item recursivly
                            the_new_child.new_child(little_child)
                self.new_child_post_action(dict_import)
            else:
                print('for now we need a name to create a parameter')
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            the_new_child = Node(parent=self, name=name, description=description, tags=tags, children=children)
            # Append this child in the self.children list
            append_child(the_new_child)
        return the_new_child


    def new_child_post_action(self, dict_import):
        """
        might be subclassed
        """
        pass

    def post_export(self, node):
        """
        export Node to a dict with all its attributes
        """
        if self.parameter:
            node.setdefault('parameter', self.parameter.export())
        else:
            node.setdefault('parameter', None)
        filiation = []
        if self.children:
            for child in self.children:
                filiation.append(child.export())
        node.setdefault('children', filiation)
        return node

    @property
    def address(self):
        """
        Current address of the node
        """
        def get_address(self):
            """
            recursive function to get into parent's hierarchy
            """
            address = spacelessify(self.name)
            if self.__class__.__name__ is not 'Device':
                if self.parent:
                    parent_address = (get_address(self.parent))
                    if self.__class__.__name__ is 'Value':
                        address = parent_address
                    else:
                        address = parent_address + '/' + address
            else:
                address = ''
            return address
        return get_address(self)
    @address.setter
    def address(self, address):
        if __dbug__:
            print('come back later for setting a new address for a node', address)
            print(self.address)
