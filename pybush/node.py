#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Node Class
The Node is based on the Basic class
It is the base class of all items in a namespace.
Device and Parameter are based on the Node Class
it 
"""
from pybush.constants import __dbug__
from pybush.functions import spacelessify
from pybush.file import File
from pybush.basic import Basic


class Node(Basic, File):
    """
    Base Class for all item in the namespace.
    It offers a way to have information / notification / functions
    about the namespace hierarchy
    It inherits from Snapshot Class. It adds recall(), snap() functions.
    This will create memories for any Node with all its chidren and attributes
    It inherits from File Class. It adds write(), read() functions.
    That export/import json files for any Node with all its chidren
    """
    def __init__(self, **kwargs):
        super(Node, self).__init__()
        # initialise attributes/properties of this node
        self._address = None
        self._parameter = None
        self._children = []
        # kwargs setup attributes
        for att, val in kwargs.items():
            setattr(self, att, val)

    def __repr__(self):
        printer = 'Node(name:{name}, description:{description}, tags:{tags}, \
                        parameter:{parameter}, children:{children})'
        return printer.format(name=self.name, description=self.description, tags=self.tags, \
                              parameter=self.parameter, children=self.children)

    # ----------- PARAMETER -------------
    @property
    def parameter(self):
        """
        parameter of the node
        """
        return self._parameter
    @parameter.setter
    def parameter(self, parameter):
        self._parameter = parameter

    # ----------- children -------------
    @property
    def children(self):
        """
        Return the list of the children registered to this node
        """
        if self._children:
            return self._children
        else:
            return []
    @children.setter
    def children(self, the_new_child):
        if the_new_child:
            if not self._children:
                self._children = [the_new_child]
            else:
                self._children.append(the_new_child)

    # ----------- NEW CHILD METHOD -------------
    def new_child(self, dict_import=None, name=None, tags=None):
        """
        Create a new Node in its parent

        You can
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        if isinstance(dict_import, dict):
            # check that the name doesn't already exists
            if self.children and 'name' in dict_import.keys():
                for child in self.children:
                    if dict_import['name'] == child.name:
                        if __dbug__:
                            print('this name is already taken by this one :', child)
                        return False
            # we import a python dict to create the child
            # be careful about children and parameter
            # which needs to instanciate Classes Node and Parameter
            the_new_child = Node(parent=self, **dict_import)
            # this will append this children as a child in the self.children list
            self.children = the_new_child
            # maybe the new_child contains children itself?
            if 'children' in dict_import.keys():
                if len(dict_import['children']) > 0:
                    for little_child in dict_import['children']:
                        # create a new child for each of the new_child.children item recursivly
                        the_new_child.new_child(little_child)
            self.new_child_post_action(dict_import)
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            the_new_child = Node(parent=self, name=name, tags=tags, children=[])
            self.children = the_new_child
        return the_new_child


    def new_child_post_action(self, dict_import):
        """
        might be subclassed
        """
        pass

    def post_export(self, node):
        """
        export Node to a json_string/python_dict with all its properties
        """
        if self.parameter:
            node.setdefault('parameter', self.parameter.export())
        filiation = []
        if self.children:
            for chili in self.children:
                filiation.append(chili.export())
        node.setdefault('children', filiation)
        return node

    # ----------- ADDRESS -------------
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
            if not address:
                address = 'no_address'
            if self.__class__.__name__ is not 'Device':
                if self.parent:
                    parent_address = (get_address(self.parent))
                    if self.__class__.__name__ is 'Parameter':
                        address = parent_address
                    else:
                        address = parent_address + '/' + address
            return address
        return get_address(self)
        #return self._address
    @address.setter
    def address(self, address):
        if __dbug__:
            print('come back later for setting a new address for a node', address)
            print(self.address)
