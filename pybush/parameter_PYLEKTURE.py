#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Parameter Class
Based on Node class
Add attributes value, clipmode, domain, unique, datatype
Add methods increment, decrement, clip
"""

from pylekture.node import Node
from pylekture.ramp import Ramp
from threading import Timer

class Parameter(Node):
    """
    A Parameter
    """
    def __init__(self, *args, **kwargs):
        super(Parameter, self).__init__()
        if self.name == 'Untitled Node':
            self.name = 'Untitled Parameter'
        if self.description == "I'm a node":
            self.description = "I'm a parameter"
        self._raw = None
        self._value = 0
        if 'datatype' in kwargs.keys():
            self.datatype = kwargs['datatype']
        else:
            self.datatype = None
        if 'clipmode' in kwargs.keys():
            self.clipmode = kwargs['clipmode']
        else:
            self.clipmode = None
        if 'unique' in kwargs.keys():
            self.unique = kwargs['unique']
        else:
            self.unique = None
        if 'domain' in kwargs.keys():
            self.domain = kwargs['domain']
        else:
            self.domain = None
        if 'value' in kwargs.keys():
            self.value = kwargs['value']
        else:
            self.value = None

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (name:{name}, description:{description}, value:{value}, datatype:{datatype}, domain:{domain}, clipmode:{clipmode}, unique:{unique}, tags:{tags})'
        return printer.format(name=self.name, description=self.description, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique, tags=self.tags)

    def clip(self, value):
        """
        clip a value to its domain according to its clipmode
            :return cliped value
        """
        if self.domain:
            if self.clipmode == 'low' or self.clipmode == 'both':
                if value < self.domain[0]:
                    value = self.domain[0]
            if self.clipmode == 'high' or self.clipmode == 'both':
                if value > self.domain[1]:
                    value = self.domain[1]
            return value
        else:
            return None

    def ramp(self, destination, duration):
        """
        Animate the parameter value

        Specify a destination and a duration.
        """
        values = Ramp(self.value, destination, duration)
        for value in values:
            self.value = value

    @property
    def raw(self):
        """
        raw value without rangeClipmode or rangeBoundsneither than datatype

        Read-only
        """
        return self._raw

    @property
    def value(self):
        """
        Current value of the parameter
        """
        if self.domain and self.datatype:
            if self.datatype == 'decimal':
                value = self.clip(self._raw)
                value = float(value)
            elif self.datatype == 'string':
                value = str(self._value)
            elif self.datatype == 'integer':
                value = self.clip(self._raw)
                value = int(value)
        else:
            value = self._value
        return value
    @value.setter
    def value(self, value):
        self._raw = value
        self._value = value

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
        Current repetitions of the parameter
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
