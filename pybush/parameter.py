#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Parameter is a node, with a value
So a Parameter inherit from Node Class and just add attributes about value
"""

from pybush.state import State
from pybush.value import Value
from pybush.automation import RampGenerator, RandomGenerator
from pybush.functions import set_attributes

class Parameter(Value):
    """
    A Parameter is always attached to a node.
    It will provide value and value's attributes to its node
    """
    def __init__(self, **kwargs):
        super(Parameter, self).__init__()
        # IMPORTANT to register parent first
        self._parent = kwargs['parent']
        # collection of states
        self._states = []
        # collection of states
        set_attributes(self, kwargs)
        # this is the player for ramp/random
        self.current_player = None

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (  address:{address}, \
                                description:{description}, \
                                raw:{raw}, value:{value}, \
                                datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                states:{states}\
                                unique:{unique}, tags:{tags})'
        return printer.format(address=self.address, description=self.description, raw=self.raw, \
                              value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique, tags=self.tags, states=len(self.states))

    @property
    def name(self):
        """
        name
        """
        return self.parent.name
    @name.setter
    def name(self, name):
        self.parent.name = name

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

    def post_export(self, export):
        """
        export the Parameter to a json_string/python_dict with all its properties
        It just adds states to the state export
        """
        snaps = []
        for snap in self.states:
            snaps.append(snap.export())
        export.setdefault('states', snaps)
        return export

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

    @property
    def parent(self):
        """
        parent of the node
        """
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def make_state(self, the_snap=None):
        """
        create a new event for this scenario
        """
        if not the_snap:
            the_snap = self.export()
        if isinstance(the_snap, dict):
            # if this is a dict, please create a state
            # it is a dict for a new snap or for an imported snap
            the_snap.setdefault('parent', self)
            the_snap = State(**the_snap)
        if isinstance(the_snap, State):
            # add the state to the states list
            self._states.append(the_snap)
            return the_snap
        else:
            return None

    @property
    def states(self):
        """
        All the events of this scenario
        """
        return self._states

    def recall(self, snap):
        """
        recall a state of the parameter
        """
        if isinstance(snap, dict):
            pass
        elif isinstance(snap, State) or isinstance(snap, State):
            snap = snap.export()
        else:
            print('ERROR 76543')
            return False
        set_attributes(self, snap)
        return True
