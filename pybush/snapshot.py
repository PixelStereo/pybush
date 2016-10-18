
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Snapshot is a parameter, with a few attributes
So a Parameter inherit from Node Class and just add attributes about value
"""
import liblo


from pybush.constants import __dbug__
from pybush.parameter import Parameter

class Snapshot(Parameter):
    """
    A Snapshot is always attached to a parameter.
    It will provide different memory of value's attributes to its parent's parameter
    """
    def __init__(self, **kwargs):
        super(Snapshot, self).__init__(**kwargs)

    def __repr__(self):
        """
        represents the parameter class
        """
        printer = 'Parameter (raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                repetitions:{repetitions}, tags:{tags})'
        return printer.format(raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              repetitions=self.repetitions, tags=self.tags)

    def get_state(self):
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

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        return {'snapshots': self.snapshots}

    @property
    def snapshots(self):
        """
        All the events of this scenario
        """
        return self._snapshots

    def new_snapshot(self):
        """
        create a new event for this scenario
        """
        the_snap = self.get_state()
        if the_snap:
            self._snapshots.append(the_snap)
            return the_snap
        else:
            return None

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
    @raw.setter
    def raw(self, value):
        pass

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
        if isinstance(self._value, list):
            # this is just a list of values to send
            for arg in self._value:
                arg = check_type(arg)
                msg.add(arg)
        else:
            msg.add(self._value)
        liblo.send(target, msg)
        if __dbug__ >= 3:
            print('update ' + self.name + ' to value ' + str(self.value))

    def recall(self, snap):
        """
        recall a snapshot
        """
        for prop, val in snap.items():
            setattr(self, prop, val)

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
