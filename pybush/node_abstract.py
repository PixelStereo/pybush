#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

import simplejson as json
from pybush.functions import prop_dict
from pybush.constants import __dbug__, _file_extention


class NodeAbstract(object):
    """
    Abstract Base Class for all item in the namespace
    Need to be subclassed
    """
    def __init__(self, parent, service='no', tags=None, priority=None):
        super(NodeAbstract, self).__init__()
        # initialise attributes/properties of this node
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority

    def __repr__(self):
        printer = 'Node (priority:{priority}, tags:{tags})'
        #return str({self.name: prop_dict(self)})
        return printer.format(name=self.name, priority=self.priority, tags=self.tags)

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

    def write(self, savepath=None):
        """
        Write a project on the hard drive.
        """
        if savepath:
            if savepath.endswith("/"):
                savepath = savepath + self.name
            # make sure we will write a file with json extension
            if not savepath.endswith('.' + _file_extention):
                savepath = savepath + '.' + _file_extention
            try:
                # create / open the file
                out_file = open((savepath), "wb")
            except IOError:
                # path does not exists
                print("ERROR 909 - path is not valid, could not save project - " + savepath)
                return False
            project = self.export()
            try:
                the_dump = json.dumps(project, sort_keys=True, indent=4,\
                                      ensure_ascii=False).encode("utf8")
            except TypeError as Error:
                print('ERROR 98 ' + str(Error))
                return False
            try:
                out_file.write(the_dump)
                print("file has been written in " + savepath)
                out_file.close()
                return True
            except TypeError as Error:
                print('ERROR 99 ' + str(Error))
                return False
        else:
            print('no filepath. Where do you want I save the project?')
            return False
