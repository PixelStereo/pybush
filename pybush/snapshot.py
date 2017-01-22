#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A Snapshot is a state of a Parameter.
"""

from pybush.functions import prop_dict
from pybush.state import State
from pybush.constants import __dbug__


class Snapshot(State):
    """
    A SnapShot is afrozen state of a param
    """
    def __init__(self, **kwargs):
        super(Snapshot, self).__init__(**kwargs)
        if 'snapshots' in kwargs.keys():
                kwargs.pop('snapshots')
        if 'name' in kwargs.keys():
                kwargs.pop('name')
        print('----INITING SNAPSHOT WITH :,', kwargs)
        for att, val in kwargs.items():
            try:
                setattr(self, att, val)
            except AttributeError as error:
                if __dbug__ == 4:
                    print(str(error) + ' ' + att)

    """def __repr__(self):
        printer = 'Snapshot (address:{address}, raw:{raw}, value:{value}, datatype:{datatype}, \
                                domain:{domain}, clipmode:{clipmode}, \
                                unique:{unique}, tags:{tags})'
        return printer.format(address=self.address, raw=self.raw, value=self.value, datatype=self.datatype, \
                              domain=self.domain, clipmode=self.clipmode, \
                              unique=self.unique, tags=self.tags)"""

