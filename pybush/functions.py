#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bunch of functions usefull for types, or namespace assertions, conventions or convertions
"""

def m_bool(value):
    """Transform to a bool if it is not already"""
    if not isinstance(value, bool):
        try:
            value = value[0]
        except:
            pass
        if value:
            value = True
        else:
            value = False
    return value

def m_int(value):
    """
    transform a list or string into an integer
    """
    if isinstance(value, list):
        value = int(value[0])
    elif not isinstance(value, int):
        value = int(value)
    return value

def m_string(value):
    """transform to a string"""
    if isinstance(value, int) or isinstance(value, float):
        value = str(value)
    elif isinstance(value, list):
        value = str(value[0])
    return value

def prop_list(the_class):
    """
    Make a list of properties presents in a class

    Args:
        an object that is an instance of a class.
        We will check what properties exists for this class

    Returns:
        A list with all properties

    Raises:
        Error: Not already implemented
    """
    the_class = the_class.__class__
    return [p for p in dir(the_class) if isinstance(getattr(the_class, p), property)]

def prop_dict(the_class):
    """
    Make a dict of properties presents in a class, with their values

    Args:
        an object that is an instance of a class.
        We will check what properties exists for this class

    Returns:
        A dict with all properties and their values

    Raises:
        Error: Not already implemented
    """
    plist = prop_list(the_class)
    pdict = {}
    for prop in plist:
        if prop == 'nodes':
            pdict.setdefault('nodes', {})
            for item in getattr(the_class, prop):
                pdict['nodes'].setdefault(item.name, prop_dict(item))
        elif prop == 'parameters':
            pdict.setdefault('parameters', {})
            for item in getattr(the_class, prop):
                pdict['parameters'].setdefault(item.name, prop_dict(item))
        else:
            pdict.setdefault(prop, getattr(the_class, prop))
    return pdict
