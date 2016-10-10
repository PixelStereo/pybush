#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Class is the root class
A project must contains devices
It might contains scenario, which is useful to drive devices
But it might it use only with devices and active mappings between input devices and output devices
"""

import os
import simplejson as json
from pybush.device import Device
from pybush.node import Node
from pybush.constants import __dbug__, __projects__, __file_extention__


def new_project(name=None):
    """
    Create a new project
    """
    new_proj = Project(name)
    __projects__.append(new_proj)
    return new_proj

def projects():
    """
    Return the list of the existing projects
    """
    return __projects__

class Project(Node):
    """
    Project class, will host devices, scenario, mappings etc…
    """
    def __init__(self, name='no-name-project', path=None):
        super(Project, self).__init__(name, None)
        self._path = path
        self._devices = []

    def __repr__(self):
        printer = 'Project (name:{name})'
        return printer.format(name=self.name)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        proj = {'devices':[]}
        for device in self.devices:
            proj['devices'].append(device.export())
        return proj

    def new_device(self, *args, **kwargs):
        """
        Create a new device
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        size = len(self._devices)
        self._devices.append(Device(args[0], self))
        for key, value in kwargs.items():
            setattr(self._devices[size], key, value)
        return self._devices[size]

    @property
    def devices(self):
        """
        return a list of devices
        """
        return self._devices

    def read(self, filepath):
        """
        Fillin Bush with objects created from a json file

        Creates Outputs, Scenario and Events obects
        First, dump attributes, then outputs, scenario and finish with events.

        :returns: True if file formatting is correct, False otherwise
        :rtype: boolean
        """
        file_content = load(filepath)
        if file_content:
            print('loading project called : ' + filepath)
        else:
            print('ERROR 901 - file provided is not a valid file' + str(filepath))
        try:
            for device_dict in file_content['devices']:
                # create a device object for all devices
                print('------- new-device : ' + device_dict['name'] + ' ------ ')
                device = self.new_device(device_dict['name'])
                # iterate each attributes of the selected device
                for prop, value in device_dict.items():
                    if prop == 'children':
                        # the device has children
                        for child in value:
                            device.new_child(child)
                    elif prop == 'parameter':
                        print('no parameter for device')
                        #device.make_parameter(value)
                    else:
                        # register value of the given attribute for the device
                        setattr(device, prop, value)
                print('device loaded : ' + device.name)
            return True
        # catch error if file is not valid or if file is not a valide node
        except (IOError, ValueError) as error:
            if __dbug__:
                print(error, "ERROR 902 - device cannot be loaded, this is not a valid Device")
            return False








def get_file_extention():
    """return the file extention"""
    file_extention = '.' + __file_extention__
    return file_extention

def load_json(path):
    """
    Load a Node from a file from hard drive
    It will play the file after loading, according to autoplay attribute value

        :arg: file to load. Filepath must be valid when provided, it must be checked before.

        :rtype:True if the node has been correctly loaded, False otherwise
    """
    content = False
    try:
        with open(path) as in_file:
            # clear the node
            content = json.load(in_file)
    # catch error if file is not valid or if file is not a Node file
    except (IOError, ValueError):
        print("ERROR 906 - node not loaded, this is not a valid Node file")
        return False
    return content

def load(path):
    """
    Read a Node file from hard drive. Must be valid.
    if valid it will be loaded and return True, otherwise, it will return False

        :param path: Filepath to read from.
        :type path: string
        :returns: Boolean
        :rtype: True if the node has been correctly loaded, False otherwise
    """
    path = os.path.abspath(path)# + get_file_extention()
    if not os.path.exists(path):
        print("ERROR 901 - THIS PATH IS NOT VALID " + path)
        return False
    else:
        print("loading JSON from " + path)
        loading = load_json(path)
        if loading:
            return loading
        else:
            return False
