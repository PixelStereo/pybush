#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
device Class is the root class
A device has some parameters and/or nodes
A device has some protocol/plugin for input/output
"""

from pybush.node import Node
from pybush.file import load
from pybush.functions import prop_dict
from pybush.constants import __dbug__, _devices

def device_new(*args, **kwargs):
    """Create a new device
        :return node object if successful
        :return False if name is not valid (already exists or is not provided)"""
    size = len(_devices)
    _devices.append(Device(args[0]))
    for key, value in kwargs.items():
        setattr(_devices[size], key, value)
    return _devices[size]

def get_devices_list():
    """return a list of devices"""
    return _devices

def devices_export():
    """Export devices"""
    devices = {}
    for device in get_devices_list():
        devices.update(device.export())
    return devices

def fillin(filepath):
    """
    Fillin Bush with objects created from a json file

    Creates Outputs, Scenario and Events obects
    First, dump attributes, then outputs, scenario and finish with events.

    :returns: True if file formatting is correct, False otherwise
    :rtype: boolean
    """
    file_content = load(filepath)
    devices = []
    if file_content: 
        print('loading device called : ' + file_content.keys()[0])
    else:
        print('ERROR 901 - file provided is not a valid file' + str(filepath))
    try:
        # dump attributes
        #print('BEFORE')
        #print(file_content)
        # itarate all devices
        for branch, content in file_content.items():
            # create a device object for all devices
            device = device_new(branch)
            # iterate each attributes of the selected device
            for prop, value in content.items():
                if prop == 'children':
                    if isinstance(value, dict):
                        # the device has children
                        for name in value.keys():
                            device.new_node(name)
                elif prop == 'service':
                    # we don't need to register this stupid property
                    pass
                else:
                    # register value of the given attribute for the device
                    setattr(device, prop, value)
            #print branch['author']
            devices.append(device)
            print('device loaded : ' + device.name)
        return devices
    # catch error if file is not valid or if file is not a valide node
    except (IOError, ValueError) as Error:
        if debug:
            print(Error, "ERROR 902 - device cannot be loaded, this is not a valid Device")
        return False


class Device(Node):
    """
    Device Class represent a device
    """
    def __init__(self, name, path=None):
        super(Device, self).__init__(name, 'no-parent')
        self._author = 'unknown'
        self._version = 'unknown'
        self._path = path
        self._name = name
        # device is a root node of a device/fixture file. So it has no parent
        # to simplify I use self, in order to always have a valid parent.name
        self._parent = self

    def __repr__(self):
        printer = 'Device (name:{name}, author:{author}, version:{version})'
        return printer.format(name=self.name, author=self.author, version=self.version)

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
        dev.update({'name':self.name, 'author':self.author, 'version':self.version, 'children':{}})
        if self.children:
            for child in self.children:
                dev['children'].update(child.export())
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
