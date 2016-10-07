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
    def __init__(self, name, parent, service='no', tags=None, priority=None, parameter=None, children=[]):
        super(Node, self).__init__(parent, service='no', tags=None, priority=None)
        # initialise attributes/properties of this node
        self._name = name
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority
        self._parameter = parameter
        self._children = children

    def __repr__(self):
        printer = 'Node (name:{name}, priority:{priority}, tags:{tags}, parameter:{parameter}, children:{children})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags, parameter=self.parameter, children=self.children)

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
            for child_0 in self.children:
                filiation.append(child_0.export())
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
    def make_parameter(self, *args, **kwargs):
        """
        Call this method to attach a parameter to this node
        You can send a string or a dict as argument
            :string : create a parameter with this name
        """
        if args:
            if self._parameter == None:
                if isinstance(args[0], dict) == True:
                    child = args[0]
                    self._parameter = Parameter(self, **child)
                else:
                    self._parameter = Parameter(self, **kwargs)
                return self._parameter
            else:
                return False
        else:
            self._parameter = Parameter(self)
            return self._parameter

  # ----------- NEW CHILD METHOD -------------
    def new_child(self, child, priority=-1, tags=None):
        """
        Create a new Node in its parent

        You can 
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        if isinstance(child, dict) == True:
            # we import a python dict to create the child
            # be careful about children and parameter which needs to instanciate Classes Node and Parameter
            assert(child, dict)
            the_new_child = Node(child['name'], self, tags=child['tags'], priority=child['priority'], children=[])
            self._children.append(the_new_child)
            # maybe the new_child contains children itself?
            if len(child['children']) > 0:
                for ch in child['children']:
                    # create a new child for each of the new_child.children item recursivly
                    little_new_child = the_new_child.new_child(ch)
            # if the new_child have a parameter, create it please
            if child['parameter']:
                # we give the parameter dict to the make_parameter method to create the parameter with values from the dict
                the_new_child.make_parameter(child['parameter'])

        else:
            # if the child argument is only a string, this is the name of the new_child to create
            the_new_child = Node(child, self, children=[])
            self._children.append(the_new_child)
        return the_new_child
