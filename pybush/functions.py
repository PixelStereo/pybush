#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bunch of functions usefull for types, or namespace assertions, conventions or convertions
"""

import simplejson as json

def m_bool(value):
    """Transform to a bool if it is not already"""
    if not isinstance(value, bool):
        # check if it is a list
        try:
            value = value[0]
        except:
            pass
        # simplify to a boolean
        value = bool(value)
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
        if prop == 'parent':
            pass
        elif prop == 'service':
            pass
        else:
            pdict.setdefault(prop, getattr(the_class, prop))
    return pdict

def load_json(filepath):
    """
    Load a Json file from a file from hard drive
    it will return the contant as a python dict 
    """
    content = False
    try:
        with open(filepath) as in_file:
            # clear the node
            content = json.load(in_file)
    # catch error if file is not valid or if file is not a Node file
    except (IOError, ValueError):
        if __dbug__:
            print("ERROR 906 - node not loaded, this is not a valid Node file")
        return False
    return content
