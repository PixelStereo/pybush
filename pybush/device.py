#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
device Class is the root class
A device has some parameters and/or nodes
A device has some protocol/plugin for input/output
"""

from pybush.node import Node
from pybush.constants import __dbug__


class Device(Node):
    """
    Device Class represent a device
    Device inherit froù Node
    Device Class creates author and version attributes
    """
    def __init__(self, name='no-name-device', parent=None):
        super(Device, self).__init__(name=name, parent=None)
        self._author = 'unknown'
        self._version = 'unknown'
        self._name = name
        # device is a root node of a device/fixture file. So it has no parent
        # to simplify I use self, in order to always have a valid parent.name
        self._parent = None

    def __repr__(self):
        printer = 'Device (name:{name}, author:{author}, version:{version}, children:{children})'
        return printer.format(name=self.name, author=self.author, \
                                version=self.version, children=self.children)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        child_export = None
        if self.children:
            child_export = []
            for child in self.children:
                child_export.append(child.export())
        return {'name':self.name, 'author':self.author, 'version':self.version, 'children':child_export}

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
