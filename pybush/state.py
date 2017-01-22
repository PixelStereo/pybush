#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A State
"""
import liblo
from pybush.constants import __dbug__
from pybush.file import File


class State(File):
    """
    A Parameter is always attached to a node.
    It will provide value and value's attributes to its node
    """
    def __init__(self, **kwargs):
        super(State, self).__init__()
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
        printer = 'State (raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                unique:{unique}, tags:{tags})'
        return printer.format(raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique, tags=self.tags)

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        param = {}
        param.setdefault('value', self.value)
        param.setdefault('domain', self.domain)
        param.setdefault('datatype', self.datatype)
        param.setdefault('clipmode', self.clipmode)
        param.setdefault('unique', self.unique)
        param.setdefault('tags', self.tags)
        return param

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

    # ----------- RAW VALUE -------------
    @property
    def raw(self):
        """
        raw value without rangeClipmode or rangeBoundsneither than datatype
        """
        return self._value

    def update(self):
        """
        update is called when value is updated
        might be used to send it to network or other protocols
        """
        ip_add = 'localhost'
        udp = 1234
        try:
            target = liblo.Address(ip_add, int(udp))
            if __dbug__ >= 3:
                print('connect to : ' + ip_add + ':' + str(udp))
        except liblo.AddressError as err:
            if __dbug__ >= 3:
                print('liblo.AddressError' + str(err))
        msg = liblo.Message(self.address)
        if isinstance(self.value, list):
            # this is just a list of values to send
            for arg in self.value:
                arg = check_type(arg)
                msg.add(arg)
        else:
            msg.add(self.value)
        liblo.send(target, msg)
        if __dbug__ >= 3:
            print('update ' + self.name + ' to value ' + str(self.value))

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

    # ----------- VALUE -------------
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
        self.update()

    # ----------- DOMAIN -------------
    @property
    def domain(self):
        """
        Current domain of the parameter
        """
        return self._domain
    @domain.setter
    def domain(self, domain):
        self._domain = domain

    # ----------- CLIPMODE -------------
    @property
    def clipmode(self):
        """
        Current clipmode of the parameter
        """
        return self._clipmode
    @clipmode.setter
    def clipmode(self, clipmode):
        self._clipmode = clipmode

    # ----------- UNIQUE -------------
    @property
    def unique(self):
        """
        Filter repetitions of the parameter
        """
        return self._unique
    @unique.setter
    def unique(self, unique):
        self._unique = unique

    # ----------- DATATYPE -------------
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

    # ----------- RAW VALUE -------------
    @property
    def raw(self):
        """
        raw value without rangeClipmode or rangeBoundsneither than datatype
        """
        return self._value

    def update(self):
        """
        update is called when value is updated
        might be used to send it to network or other protocols
        """
        ip_add = 'localhost'
        udp = 1234
        try:
            target = liblo.Address(ip_add, int(udp))
            if __dbug__ >= 3:
                print('connect to : ' + ip_add + ':' + str(udp))
        except liblo.AddressError as err:
            if __dbug__ >= 3:
                print('liblo.AddressError' + str(err))
        msg = liblo.Message(self.address)
        if isinstance(self.value, list):
            # this is just a list of values to send
            for arg in self.value:
                arg = check_type(arg)
                msg.add(arg)
        else:
            msg.add(self.value)
        liblo.send(target, msg)
        if __dbug__ >= 3:
            print('update ' + self.name + ' to value ' + str(self.value))
