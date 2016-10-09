
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Parameter is a node, with a value
So a Parameter inherit from Node Class and just add attributes about value
"""

from pybush.constants import __dbug__
from pybush.node_abstract import NodeAbstract

class Parameter(NodeAbstract):
    """
    A Parameter is always attached to a node.
    It will provide value and value's attributes to its parent's node
    """
    def __init__(self, parent=None, raw=None, value=None, datatype=None, tags=None, \
                    priority=None, domain=None, clipmode=None, repetitions=True):
        super(Parameter, self).__init__(parent=parent)
        self._value = value
        self._clipmode = clipmode
        self._domain = domain
        self._repetitions = repetitions
        self._datatype = datatype
        self._service = 'xXx'
        self._raw = raw
        # herited from the parent's node
        self.name = parent.name
        self.priority = parent.priority
        self.tags = parent.tags

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                repetitions:{repetitions}, priority:{priority}, tags:{tags})'
        return printer.format(raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              repetitions=self.repetitions, priority=self.priority, tags=self.tags)

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        param = {}
        param.setdefault('raw', self.value)
        param.setdefault('value', self.value)
        param.setdefault('domain', self.domain)
        param.setdefault('datatype', self.datatype)
        param.setdefault('clipmode', self.clipmode)
        param.setdefault('repetitions', self.repetitions)
        return param

    def set(self, state_dict):
        """
        Set a parameter to a state
        """
        for prop, val in state_dict:
            setattr(self, prop, val)

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
        print('update ' + self.name + ' to value ' + str(self.value))

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

    # ----------- REPETITIONS -------------
    @property
    def repetitions(self):
        """
        Current repetitions of the parameter
        """
        return self._repetitions
    @repetitions.setter
    def repetitions(self, repetitions):
        self._repetitions = repetitions

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
