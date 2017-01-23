#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
All the Exceptions declared by the package are here
---
"""

class BushTypeError(Exception):
    """
    Waiting for an object of class 'expected', but received an object of class 'received'
    """
    def __init__(self, expected, received):
        super(BushTypeError, self).__init__()
        self.error_code = 1
        dbg = 'Wait for an {expected} instance object but receive a {received}'
        print(dbg.format(expected=expected, received=received.__class__))

class NoOutputError(Exception):
    """
    There is no output in this device
    """
    def __init__(self):
        super(NoOutputError, self).__init__()
        self.error_code = 401
