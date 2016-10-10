#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Class is the root class
A project must contains devices
It might contains scenario, which is useful to drive devices
But it might it use only with devices and active mappings between input devices and output devices
"""

from pybush.device import Device
from pybush.constants import __dbug__, __projects__
from pybush.node_abstract import NodeAbstract
from pybush.file import File

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

class Project(NodeAbstract, File):
    """
    Project class, will host devices, scenario, mappings etc…
    """
    def __init__(self, name='no-name-project', parent=None):
        super(Project, self).__init__(name=name, parent=parent)
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
        print(proj)
        return proj

    def new_device(self, *args, **kwargs):
        """
        Create a new device
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        size = len(self._devices)
        self._devices.append(Device(name=args[0], parent=self))
        for key, value in kwargs.items():
            setattr(self._devices[size], key, value)
        return self._devices[size]

    @property
    def devices(self):
        """
        return a list of devices
        """
        return self._devices

    def load(self, filepath):
        """
        Fillin Bush with objects created from a json file

        Creates Outputs, Scenario and Events obects
        First, dump attributes, then outputs, scenario and finish with events.

        :returns: True if file formatting is correct, False otherwise
        :rtype: boolean
        """
        # self.read is a method from File Class
        file_content = self.read(filepath)
        # TODO : CHECK IF THIS IS A VALID PROJECT FILE
        # if valid python dict / json file
        if file_content:
            if __dbug__:
                print('loading project called : ' + filepath)
        else:
            if __dbug__:
                print('ERROR 901 - file provided is not a valid file' + str(filepath))
        try:
            for device_dict in file_content['devices']:
                # create a device object for all devices
                if __dbug__:
                    print('------- new-device : ' + device_dict['name'] + ' ------ ')
                device = self.new_device(device_dict['name'])
                # iterate each attributes of the selected device
                for prop, value in device_dict.items():
                    if prop == 'children':
                        # the device has children
                        for child in value:
                            device.new_child(child)
                    elif prop == 'parameter':
                        if __dbug__:
                            print('no parameter for device')
                        #device.make_parameter(value)
                    else:
                        # register value of the given attribute for the device
                        setattr(device, prop, value)
                if __dbug__:
                    print('device loaded : ' + device.name)
            return True
        # catch error if file is not valid or if file is not a valide node
        except (IOError, ValueError) as error:
            if __dbug__:
                print(error, "ERROR 902 - device cannot be loaded, this is not a valid Device")
            return False
