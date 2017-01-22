#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Class is the root class
A project must contains devices
it might be used with devices and active mappings between
input devices and output device
"""

import datetime
from pybush import __version__
from pybush.device import Device
from pybush.constants import __dbug__, __projects__

def new_project(name=None):
    """
    Create a new project
    """
    new_proj = Project(name=name)
    __projects__.append(new_proj)
    return new_proj

def projects():
    """
    Return the list of the existing projects
    """
    return __projects__

class Project(Device):
    """
    Project class, will host devices, mappings etc…
    Project inherits from Device because it might have input/outputs
    TODO:control each function/attribute from/to a device with OSC/ARTNET/MIDI
    """
    def __init__(self, **kwargs):
        super(Project, self).__init__(**kwargs)
        self._devices = []
        # from pylekture
        self._lastopened = None
        self._created = str(datetime.datetime.now())
        self._version = __version__

    def reset(self):
        """
        reset a project by deleting project.attributes related
        """
        # reset project attributes
        self._version = None
        self._path = None
        if self.devices != []:
            for dev in self.devices:
                del dev
        if self.children != []:
            for child in self.children:
                del child
        self.children = []
        self.devices = []
        self._created = str(datetime.datetime.now())

    def __repr__(self):
        printer = 'Project (name:{name})'
        return printer.format(name=self.name)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        proj = {'devices':[], 'lastopened':self.lastopened, \
                'version':self.version,'created':self.created }
        if self.devices != []:
            for device in self.devices:
                proj['devices'].append(device.export())
        return proj

    def new_device(self, dict_import=None, name=None, tags=None, version=None, author=None):
        """
        Create a new device
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        if isinstance(dict_import, dict):
            # we import a python dict to create the child
            # be careful about children and parameter
            # which needs to instanciate Classes Node and Parameter
            self.devices = Device (parent=None, name=dict_import['name'],
                                    version=dict_import['version'], author=dict_import['author'], \
                                    tags=dict_import['tags'])
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            self.devices = Device(name=name, tags=tags, version=version, author=author)
        return self.devices[-1]

    @property
    def devices(self):
        """
        return a list of devices
        """
        return self._devices
    @devices.setter
    def devices(self, the_new_device):
        if the_new_device:
            if self._devices is None:
                self._devices = [the_new_device]
            else:
                self._devices.append(the_new_device)
            return True
        else:
            return False

    @property
    def lastopened(self):
        """
        Datetime of the last opened date of this project. Default is None

        :getter: datetime object
        :type getter: string
        """
        return self._lastopened

    @property
    def created(self):
        """
        Datetime of the creation of the project

        :getter: datetime object
        :type getter: string
        """
        return self._created

    def load(self, filepath):
        """
        Fillin Bush with objects created from a json file

        Creates Outputs obects
        First, dump attributes, then outputs.

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
                    if value:
                        if prop == 'children':
                            for child in value:
                                device.new_child(child)
                        elif prop == 'parameter':
                            if __dbug__:
                                print('no parameter for device')
                                #device.make_parameter(value)
                        elif prop == 'outputs':
                            if __dbug__:
                                print('import will create an output')
                            device.new_output(value)
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
