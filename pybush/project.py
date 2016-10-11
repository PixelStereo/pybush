#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Class is the root class
A project must contains devices
It might contains scenario, which is useful to drive devices
But it might it use only with devices and active mappings between input devices and output devices
"""

import datetime
from pybush import __version__
from pybush.device import Device
from pybush.constants import __dbug__, __projects__

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

class Project(Device):
    """
    Project class, will host devices, scenario, mappings etc…
    """
    def __init__(self, name='no name project', description='Project without name', \
                    parent=None):
        super(Project, self).__init__(name=name, parent=parent, description=description)
        self._devices = []
        # from pylekture
        self._lastopened = None
        self._created = str(datetime.datetime.now())
        self._scenarios = []
        self._events = []
        self._version = __version__

    def reset(self):
        """reset a project by deleting project.attributes, scenarios and events related"""
        # reset project attributes
        self._version = None
        self._path = None
        # reset scenarios
        self._scenarios = []
        # reset  events
        self._events = []

    def __repr__(self):
        printer = 'Project (name:{name})'
        return printer.format(name=self.name)

    """def __repr__(self):
        s = "Project (name={name}, path={path}, description={description}, tags={tags}, autoplay={autoplay}, loop={loop}, " \
            "scenarios={scenarios}, events={events})"
        return s.format(name=self.name,
                        path=self.path,
                        description=self.description,
                        tags=self.tags,
                        autoplay=self.autoplay,
                        loop=self.loop,
                        scenarios=len(self.scenarios),
                        events=len(self.events))
    """

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        proj = {'devices':[]}
        for device in self.devices:
            proj['devices'].append(device.export())
        return proj

    """def export(self):

        export = {}
        export.setdefault('attributes', {})
        for key, value in prop_dict(self).items():
            if key == 'events':
                events = []
                for event in value:
                    events.append(event.export())
                export.setdefault('events', events)
            elif key == 'scenarios':
                scenarios = []
                for scenario in value:
                    scenarios.append(scenario.export())
                export.setdefault('scenarios', scenarios)
            else:
                export['attributes'].setdefault(key, value)
        export['attributes'].pop('parent')
        return export



        # create a dict to export the content of the node
        export = {}
        # this is the dictionary of all props (output is already processed)
        props = prop_dict(self)
        # just the keys please
        keys = props.keys()
        for key in keys:
            # for an output, we just need the index, not the output object
            if key == 'output':
                if props['output']:
                    if props['output'] in self.parent.outputs:
                        export.setdefault('output', self.parent.outputs.index(props['output']) + 1)
                else:
                    export.setdefault('output', 0)
            elif key == 'events':
                # for an event, we just need the index, not the event object
                export.setdefault('events', [])
                if props['events']:
                    for event in props['events']:
                        if event.__class__.__name__ == "ScenarioPlay":
                            export.setdefault('events', [])
                        else:
                            export['events'].append(self.parent.events.index(event))
                else:
                    export.setdefault('events', [])
            else:
                # this is just a property, dump them all !!
                export.setdefault(key, props[key])
        # Itarate a second time to link ScenarioPlay obkects with Scenario
        for key in keys:
            if key == 'events':
                if props['events']:
                    for event in props['events']:
                        if event.__class__.__name__ == "ScenarioPlay":
                            export['events'].append(self.parent.events.index(event))
        # we don't need parent in an export, because the JSON/dict export format do that
        export.pop('parent')
        return export
    """

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
            self.devices = Device(name=dict_import['name'], parent=self, \
                                    version=dict_import['version'], author=dict_import['author'], \
                                    tags=dict_import['tags'])
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            self.devices = Device(name=name, parent=self, tags=tags, version=version, author=author)
        return self.devices[-1]

    @property
    def devices(self):
        """
        return a list of devices
        """
        return self._devices
    @devices.setter
    def devices(self, the_new_device):
        if self._devices is None:
            self._devices = [the_new_device]
        else:
            self._devices.append(the_new_device)

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
                    if value:
                        if prop == 'children':
                            # the device has children
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
