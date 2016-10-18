
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

    def export(self):
        """
        export the Parameter to a json_string/python_dict with all its properties
        """
        return {'snapshots': self.snapshots}
