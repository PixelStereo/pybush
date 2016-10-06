#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
device Class is the root class
A device has some parameters and/or nodes
A device has some protocol/plugin for input/output
"""

from pybush.node import Node
from pybush.functions import prop_dict
from pybush.constants import __dbug__
from pybush.file import load


class Device(Node):
    """
    Device Class represent a device
    """
    def __init__(self, name='no-name-device', path=None):
        super(Device, self).__init__(name, 'no-parent-for-a-Device')
        self._author = 'unknown'
        self._version = 'unknown'
        self._path = path
        self._name = name
        # device is a root node of a device/fixture file. So it has no parent
        # to simplify I use self, in order to always have a valid parent.name
        self._parent = self

    def __repr__(self):
        printer = 'Device (name:{name}, author:{author}, version:{version}, children:{children})'
        return printer.format(name=self.name, author=self.author, version=self.version, children=self.children)

    @property
    def path(self):
        """
        This is the filepath where to write the file or where it is located.
        It's initialised at None when created, and can be set to any valid path.

        :param path: valid filepath. Return True if valid, False otherwise.
        :type path: string
        """
        return self._path
    @path.setter
    def path(self, value):
        self._path = value
        
    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        dev = {}
        dev.update({'name':self.name, 'author':self.author, 'version':self.version, 'children':[]})
        if self.children:
            for child in self.children:
                dev['children'].append(child.export())
        return dev

    # ----------- AUTHOR -------------
    @property
    def author(self):
        """
        Current author of the device
        """
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
    @author.deleter
    def author(self):
        return False

    # ----------- VERSION -------------
    @property
    def version(self):
        """
        Current version of the device
        """
        return self._version
    @version.setter
    def version(self, version):
        self._version = version
    @version.deleter
    def version(self):
        return False
