#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Parameter is a node, with a value
So a Parameter inherit from Node Class and just add attributes about value
"""
import liblo
from pybush.constants import __dbug__
from pybush.state import State
from pybush.snapshot import Snapshot
from pybush.automation import RampGenerator, RandomGenerator


class Parameter(State):
    """
    A Parameter is always attached to a node.
    It will provide value and value's attributes to its node
    """
    def __init__(self, **kwargs):
        super(Parameter, self).__init__()
        # IMPORTANT to register parent first
        self._parent = kwargs['parent']
        # collection of snapshots
        self._snapshots = []
        # collection of snapshots
        for att, val in kwargs.items():
            if att == 'snapshots':
                for snap in kwargs[att]:
                    self.snap(snap)
            else:
                try:
                    setattr(self, att, val)
                except(AttributeError) as error:
                    if __dbug__ == 4:
                        print(str(error) + ' ' + att)
        self._value = 0.
        self._clipmode = None
        self._domain = None
        self._unique = None
        self._datatype = None
        self._raw = None
        for key in kwargs.keys():
            setattr(self, '_'+key, kwargs[key])
        # there is no animation on the param
        self.current_player = None

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (address:{address}, description:{description}, raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                unique:{unique}, tags:{tags})'
        return printer.format(address=self.address, description=self.description, raw=self.raw, \
                              value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique, tags=self.tags)

    @property
    def address(self):
        """
        address
        """
        return self.parent.address

    @property
    def description(self):
        """
        description
        """
        return self.parent.description
    @description.setter
    def description(self, description):
        self.parent.description = description


    @property
    def tags(self):
        """
        address
        """
        return self.parent.tags
    @tags.setter
    def tags(self, tags):
        self.parent.tags = tags

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        param = {}
        #param.setdefault('name', self.name)
        snaps = []
        for snap in self.snapshots:
            if not isinstance(snap, dict):
                snaps.append(snap.export())
            else:
                snaps.append(snap)
        param.setdefault('snapshots', snaps)
        param.setdefault('value', self.value)
        param.setdefault('domain', self.domain)
        param.setdefault('datatype', self.datatype)
        param.setdefault('clipmode', self.clipmode)
        param.setdefault('unique', self.unique)
        param.setdefault('tags', self.tags)
        return param

    def recall(self, snap):
        """
        recall a snapshot of the parameter
        """
        for prop, val in snap.export().items():
            if prop == 'name' or prop == 'raw':
                pass
            else:
                setattr(self, prop, val)

    def ramp(self, destination=1, duration=1000, grain=10):
        """
        ramp is an animation that drive from the current value to another in a certain time
        destination : value to reach
        duration : duration of the ramp
        grain : time between each grain
        """
        if self.current_player:
            self.current_player.terminate()
        self.current_player = RampGenerator(self, self.value, destination, duration, grain)
        return self.current_player

    def random(self, destination=1, duration=1000, grain=10):
        """
        random is an animation that generate pseudo random valuesin a certain time
        duration : duration of the ramp
        grain : time between each grain
        """
        if self.current_player:
            self.current_player.terminate()
        self.current_player = RandomGenerator(self, self.value, destination, duration, grain)
        return self.current_player

    def new_child_post_action(self, dict_import):
        """
        might be subclassed if need to do something with the 
        """
        # if the new_child have a parameter, create it please
        if dict_import['parameter']:
            # we give the parameter dict to the make_parameter method
            # it will create the parameter with values from the dict
            if the_new_child.make_parameter(dict_import['parameter']):
                return True
            else:
                return False

    # ----------- PARENT -------------
    @property
    def parent(self):
        """
        parent of the node
        """
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def snap(self, name, the_snap=None):
        """
        create a new event for this scenario
        """
        if not the_snap:
            the_snap = self.export()
        if isinstance(the_snap, dict):
            # if this is a dict, please create a snapshot
            # it is a dict for a new snap or for an imported snap
            the_snap.setdefault('parent', self)
            the_snap = Snapshot(**the_snap)
        if the_snap:
            # used to load an existing project and load a snap_dict
            self._snapshots.append(the_snap)
            return the_snap
        else:
            return None

    @property
    def snapshots(self):
        """
        All the events of this scenario
        """
        return self._snapshots
