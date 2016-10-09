#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Node is the Base class of all items in a namespace.
Application and Parameter are based on the Node Class
"""

import simplejson as json
from pybush.constants import __dbug__, __file_extention__


class NodeAbstract(object):
    """
    Abstract Base Class for all item in the namespace
    Need to be subclassed
    """
    def __init__(self, parent=None, service=None, tags=None, priority=None):
        super(NodeAbstract, self).__init__()
        # initialise attributes/properties of this node
        self._parent = parent
        self.service = service
        self._tags = tags
        self._priority = priority

    def __repr__(self):
        printer = 'AbstractNode (priority:{priority}, tags:{tags})'
        return printer.format(priority=self.priority, tags=self.tags)

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
        print('ask for parent of ', self)
        return self._parent.name

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

    def write(self, savepath=None):
        """
        Write a project on the hard drive.
        """
        if savepath:
            if savepath.endswith("/"):
                savepath = savepath + self.name
            # make sure we will write a file with json extension
            if not savepath.endswith('.' + __file_extention__):
                savepath = savepath + '.' + __file_extention__
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
            except TypeError as error:
                print('ERROR 98 ' + str(error))
                return False
            try:
                out_file.write(the_dump)
                print("file has been written in " + savepath)
                out_file.close()
                return True
            except TypeError as error:
                print('ERROR 99 ' + str(error))
                return False
        else:
            print('no filepath. Where do you want I save the project?')
            return False
