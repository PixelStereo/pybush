#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A State
"""
import liblo
from pybush.constants import __dbug__
from pybush.file import File
from pybush.functions import check_type


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
                                unique:{unique}'
        return printer.format(raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique)

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        state = {}
        state.setdefault('value', self.value)
        state.setdefault('domain', self.domain)
        state.setdefault('datatype', self.datatype)
        state.setdefault('clipmode', self.clipmode)
        state.setdefault('unique', self.unique)
        state = self.post_export(state)
        return state

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
        for out in self.parent.get_device().outputs:
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
    def datatype(self):
        """
        Current datatype of the parameter
        could be None (default), or string, integer, decimal
        """
        return self._datatype
    @datatype.setter
    def datatype(self, datatype):
        self._datatype = datatype
