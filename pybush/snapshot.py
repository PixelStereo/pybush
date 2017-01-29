#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Snapshot is a state of a Parameter.
"""

from pybush.state import State
from pybush.basic import Basic
from pybush.constants import __dbug__
from pybush.functions import set_attributes


class Snapshot(State, Basic):
    """
    A SnapShot is afrozen state of a param
    """
    def __init__(self, **kwargs):
        super(Snapshot, self).__init__(**kwargs)
        if __dbug__:
            print('-- creating a snapshot --')
        # Don't store snapshots or name
        # We only want a state to store, and basics (name, description, tags)
        # for the snapshot
        if 'snapshots' in kwargs.keys():
            kwargs.pop('snapshots')
        if 'name' in kwargs.keys():
            kwargs.pop('name')
        set_attributes(self, kwargs)

    def __repr__(self):
        printer = 'Snapshot(name:{name}, description:{description}, \
                            raw:{raw}, value:{value}, datatype:{datatype}, \
                            domain:{domain}, clipmode:{clipmode}, \
                            unique:{unique}, tags:{tags})'
        return printer.format(  name=self.name,
                                description=self.description, \
                                raw=self.raw,
                                value=self.value, \
                                datatype=self.datatype,
                                domain=self.domain, \
                                clipmode=self.clipmode,
                                unique=self.unique, \
                                tags=self.tags)

    def post_export(self, export):
        return export
