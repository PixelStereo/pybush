#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
Value
A Value can be integer - decimal - string - array
"""
import liblo
from pybush.functions import set_attributes
from pybush.automation import RampGenerator, RandomGenerator
from pybush.errors import NoOutputError
from pybush.constants import __dbug__

class Value(object):
    """
    A Value is an abstract class for creating a typed value
    It provides value attributes
    """
    def __init__(self, **kwargs):
        super(Value, self).__init__()
        if 'parent' in kwargs.keys():
            self._parent = kwargs['parent']
        self._value = None
        self._clipmode = None
        self._domain = None
        self._silent = False
        self._unique = None
        self._datatype = None
        self._raw = None
        # initialise attributes/properties of this node
        set_attributes(self, kwargs)
        # there is no animation on the param
        self._current_player = None

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Value (raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                unique:{unique}'
        return printer.format(raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique)

    @property
    def raw(self):
        """
        raw value without rangeClipmode or rangeBoundsneither than datatype
        """
        return self._value

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

    @property
    def silent(self):
        """
        address
        """
        return self._silent
    @silent.setter
    def silent(self, silent):
        self._silent = silent

    @property
    def value(self):
        """
        Current value of the parameter
        """
        if self.datatype == 'decimal':
            value = self.clip(self._value)
            value = float(value)
        elif self.datatype == 'string':
            value = str(self._value)
        elif self.datatype == 'integer':
            value = self.clip(self._value)
            value = int(self._value)
        else:
            value = self._value
        return value
    @value.setter
    def value(self, value):
        self._value = value
        if self.silent or not self.parent.get_device().outputs:
            return
        self.update()

    def clip(self, value):
        """
        clip a value to its domain according to its clipmode
            :return cliped value
        """
        if self.clipmode == 'low' or self.clipmode == 'both':
            if len(self.domain) > 0:
                if value < self.domain[0]:
                    value = self.domain[0]
        if self.clipmode == 'high' or self.clipmode == 'both':
            if len(self.domain) > 1:
                if value > self.domain[1]:
                    value = self.domain[1]
        return value

    def update(self):
        """
        update is called when value is updated
        might be used to send it to network or other protocols
        """
        for out in self.parent.get_device().outputs:
            try:
                split = out.port.split(':')
                ip_add = split[0]
                udp = split[1]
                try:
                    target = liblo.Address(ip_add, int(udp))
                    if __dbug__ >= 3:
                        print('connect to : ' + ip_add + ':' + str(udp))
                except liblo.AddressError as err:
                    if __dbug__ >= 3:
                        print('liblo.AddressError' + str(err))
                msg = liblo.Message('/' + self.address)
                if isinstance(self.value, list):
                    # this is a list of values to send
                    for arg in self.value:
                        arg = check_type(arg)
                        msg.add(arg)
                else:
                    # this is a single value to send
                    msg.add(self.value)
                liblo.send(target, msg)
                if __dbug__ >= 3:
                    print('update ' + self.name + ' to value ' + str(self.value))
                return True
            except NoOutputError:
                return False

    @property
    def domain(self):
        """
        Current domain of the parameter
        """
        return self._domain
    @domain.setter
    def domain(self, domain):
        self._domain = domain

    @property
    def clipmode(self):
        """
        Current clipmode of the parameter
        """
        return self._clipmode
    @clipmode.setter
    def clipmode(self, clipmode):
        self._clipmode = clipmode

    @property
    def unique(self):
        """
        Filter repetitions of the parameter
        """
        return self._unique
    @unique.setter
    def unique(self, unique):
        self._unique = unique

    @property
    def parent(self):
        """
        Current parent of the parameter
        """
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def datatype(self):
        """
        Current datatype of the parameter
        could be None (default), or string, integer, decimal
        """
        return self._datatype
    @datatype.setter
    def datatype(self, datatype):
        self._datatype = datatype

    def export(self):
        """
        export the Value to a json_string/python_dict with all its properties
        """
        state = {}
        state.setdefault('value', self.value)
        state.setdefault('domain', self.domain)
        state.setdefault('datatype', self.datatype)
        state.setdefault('clipmode', self.clipmode)
        state.setdefault('unique', self.unique)
        state = self.post_export(state)
        return state

    def post_export(self, state):
        """
        append Value to a dict with all its attributes
        """
        return state

    def ramp(self, destination=1, duration=1000, grain=10):
        """
        ramp is an animation that drive from the current value to another in a certain time
        destination : value to reach
        duration : duration of the ramp
        grain : time between each grain
        """
        if self._current_player:
            self._current_player.terminate()
        self._current_player = RampGenerator(self, self.value, destination, duration, grain)
        return self._current_player

    def random(self, destination=1, duration=1000, grain=10):
        """
        random is an animation that generate pseudo random valuesin a certain time
        duration : duration of the ramp
        grain : time between each grain
        """
        if self._current_player:
            self._current_player.terminate()
        self._current_player = RandomGenerator(self, self.value, destination, duration, grain)
        return self._current_player

class Numeric(Value):
    """
    A numeric value might be a decimal or an integer.
    It can support automation
    """
    def __init__(self, value=None, domain=None, clipmode=None):
        super(Numeric, self).__init__()
        # initialise attributes/properties of this node
        set_attributes(self, kwargs)


class Integer(Numeric):
    """
    An Integer is a numeric integer value
    """
    def __init__(self, **kwargs):
        super(Integer, self).__init__()
        # initialise attributes/properties of this node
        set_attributes(self, kwargs)
