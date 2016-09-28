#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
device Class is the root class
An device has some leaves and/or nodes
An device has some protocol/plugin for input/output
"""

from pybush.node import Node
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
    devices = {'devices':{}}
    for device in get_devices_list():
        devices['devices'].setdefault(device.name, {'attributes': \
            {'author':device.author, 'name':device.name, 'version':device.version}})
        if device.nodes:
            devices['devices'][device.name].setdefault('nodes', {})
            for node in device.nodes:
                devices['devices'][device.name]['nodes'].setdefault(node.name, prop_dict(node))
    return devices


class Device(Node):
    """device Class"""
    def __init__(self, name):
        super(Device, self).__init__(name)
        self._author = 'unknown'
        self._version = 'unknown'
        self._name = name

    def __repr__(self):
        printer = 'device (name:{name}, author:{author}, version:{version})'
        return printer.format(name=self.name, author=self.author, version=self.version)

    # ----------- AUTHOR -------------
    @property
    def author(self):
        "Current author of the device"
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
        "Current version of the device"
        return self._version
    @version.setter
    def version(self, version):
        self._version = version
    @version.deleter
    def version(self):
        return False
