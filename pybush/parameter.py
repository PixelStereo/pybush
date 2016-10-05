
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Parameter is a node, with a value
So a Parameter inherit from Node Class and just add attributes about value
"""

from pybush.constants import __dbug__

class Parameter(object):
    """
    A Parameter is always attached to a node.
    It will provide value and value's attributes to its parent's node
    """
    def __init__(self, parent):
        super(Parameter, self).__init__()
        self._value = None
        self._clipmode = None
        self._domain = None
        self._repetitions = 0
        self._datatype = 'generic'
        self._service = 'xXx'
        # herited from the parent's node
        self.name = parent.name
        self.priority = parent.priority
        self.tags = parent.tags

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (name:{name}, value:{value}, datatype:{datatype}, domain:{domain}, clipmode:{clipmode}, repetitions:{repetitions}, priority:{priority}, tags:{tags})'
        return printer.format(name=self.name, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              repetitions=self.repetitions, priority=self.priority, tags=self.tags)

    @property
    def service(self):
        """
        Return the service of the node
        """
        return self.__class__.__name__
    @service.setter
    def service(self, service):
        pass

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        param = {}
        param.setdefault('value', self.value)
        param.setdefault('domain', self.domain)
        param.setdefault('datatype', self.datatype)
        param.setdefault('clipmode', self.clipmode)
        param.setdefault('repetitions', self.repetitions)
        return param

    def clip(self, value):
        """
        clip a value to its domain according to its clipmode
            :return cliped value
        """
        if self.clipmode == 'low' or self.clipmode == 'both':
            if value < self.domain[0]:
                value = self.domain[0]
        if self.clipmode == 'high' or self.clipmode == 'both':
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
    @value.deleter
    def value(self):
        return False

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
    @domain.deleter
    def domain(self):
        return False

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
    @clipmode.deleter
    def clipmode(self):
        return False

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
    @repetitions.deleter
    def repetitions(self):
        return False

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
    @datatype.deleter
    def datatype(self):
        return False
