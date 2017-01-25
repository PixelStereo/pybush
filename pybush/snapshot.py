#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Snapshot is a state of a Parameter.
"""

from pybush.state import State
from pybush.basic import Basic
from pybush.constants import __dbug__


class Snapshot(State, Basic):
    """
    A SnapShot is afrozen state of a param
    """
    def __init__(self, **kwargs):
        super(Snapshot, self).__init__(**kwargs)
        if __dbug__:
            print('----------------creating a snapshot----------------')
        if 'snapshots' in kwargs.keys():
            kwargs.pop('snapshots')
        if 'name' in kwargs.keys():
            kwargs.pop('name')
        for att, val in kwargs.items():
            try:
                setattr(self, att, val)
            except AttributeError as error:
                if __dbug__ == 4:
                    print(str(error) + ' ' + att)

    def __repr__(self):
        printer = 'Snapshot(name:{name}, description:{description}, \
                            raw:{raw}, value:{value}, datatype:{datatype}, \
                            domain:{domain}, clipmode:{clipmode}, \
                            unique:{unique}, tags:{tags})'
        return printer.format(  name=self.name, description=self.description, \
                                raw=self.raw, value=self.value, \
                                datatype=self.datatype, domain=self.domain, \
                                clipmode=self.clipmode, unique=self.unique, \
                                tags=self.tags)
