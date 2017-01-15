#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

from pybush.constants import __dbug__
from pybush.node_abstract import NodeAbstract
from pybush.parameter import Parameter
from pybush.file import File

class Node(NodeAbstract, File):
    """Base Class for all item in the namespace"""
    def __init__(self, **kwargs):
        super(Node, self).__init__()
        # initialise attributes/properties of this node
        self._parameter = None
        self._children = []
        # kwargs setup attributes
        for att, val in kwargs.items():
            setattr(self, att, val)

    def __repr__(self):
        printer = 'Node (name:{name}, parameter:{parameter}, children:{children})'
        return printer.format(name=self.name, parameter=self.parameter, children=self.children)

    def new_snapshot(self, **kwargs):
        """
        method to call parameter's snapshot
        """
        return self.export()

    def recall(self, *args, **kwargs):
        """
        Method to recall a snapshot of a parameter
        """
        if self.parameter:
            return self.parameter.recall(*args, **kwargs)
        else:
            return False


    @property
    def snapshots(self):
        """
        Ordered list of snapshots
        """
        if self.parameter:
            return self.parameter.snapshots
        else:
            return False

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
            for chili in self.children:
                filiation.append(chili.export())
        return {'name':self.name, 'tags':self.tags, 'children':filiation, 'parameter':param}

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
    def parameter(self, *args, **kwargs):
        if args:
            if __dbug__:
                print('why to do with that')
        elif kwargs:
            self._parameter.set(kwargs)

    # ----------- MAKE_PARAMETER METHOD -------------
    def make_parameter(self, *args, **kwargs):
        """
        Call this method to attach a parameter to this node
        You can send a string or a dict as argument
        string : create a parameter with this name
        """
        if args:
            if self._parameter is None:
                if isinstance(args[0], dict):
                    child = args[0]
                    child.setdefault('parent', self)
                    self._parameter = Parameter(**child)
                else:
                    kwargs.setdefault('parent', self)
                    self._parameter = Parameter(**kwargs)
                return self._parameter
            else:
                return False
        else:
            self._parameter = Parameter(parent=self)
            return self._parameter

  # ----------- NEW CHILD METHOD -------------
    def new_child(self, dict_import=None, name=None, tags=None):
        """
        Create a new Node in its parent

        You can
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        if isinstance(dict_import, dict):
            # we import a python dict to create the child
            # be careful about children and parameter
            # which needs to instanciate Classes Node and Parameter
            the_new_child = Node(parent=self, name=dict_import['name'], tags=dict_import['tags'], children=[])
            # this will append this children as a child in the self.children list
            self.children = the_new_child
            # maybe the new_child contains children itself?
            if dict_import['children']:
                if len(dict_import['children']) > 0:
                    for little_child in dict_import['children']:
                        # create a new child for each of the new_child.children item recursivly
                        the_new_child.new_child(little_child)
            # if the new_child have a parameter, create it please
            if dict_import['parameter']:
                # we give the parameter dict to the make_parameter method
                # it will create the parameter with values from the dict
                the_new_child.make_parameter(dict_import['parameter'])
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            the_new_child = Node(parent=self, name=name, tags=tags, children=[])
            self.children = the_new_child
        return the_new_child
