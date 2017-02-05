#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A State is a copy of a Value at a certain state
"""

from pybush.value import Value
from pybush.basic import Basic
from pybush.constants import __dbug__
from pybush.functions import set_attributes


class State(Value, Basic):
    """
    A State is afrozen state of a param
    """
    def __init__(self, **kwargs):
        super(State, self).__init__(**kwargs)
        if __dbug__:
            print('creating a state')
        set_attributes(self, kwargs)

    def __repr__(self):
        printer =     'State(name:{name}, '\
                            'description:{description}, '\
                            'tags:{tags}, '\
                            'raw:{raw}, '\
                            'value:{value}, '\
                            'datatype:{datatype}, '\
                            'domain:{domain}, '\
                            'clipmode:{clipmode}, '\
                        'unique:{unique})'
        return printer.format(  name=self.name,\
                                description=self.description, \
                                tags=self.tags,\
                                raw=self.raw,\
                                value=self.value, \
                                datatype=self.datatype,
                                domain=self.domain, \
                                clipmode=self.clipmode, \
                                unique=self.unique)
