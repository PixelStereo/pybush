#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bunch of functions usefull for types, or namespace assertions, conventions or convertions
"""

import re
import simplejson as json
from pybush.constants import __dbug__


def check_type(data):
    """
    Transform an unicode into its original type

    data:
        an integer or float encoded as a string

    Returns:
        an integer or a float
    """
    try:
        if len(data) == 1 and isinstance(data, list):
            data = data[0]
    except TypeError:
        pass
    try:
        if data.isdigit():
            data = int(data)
        else:
            try:
                data = float(data)
            except ValueError:
                pass
    except AttributeError:
        pass
    return data

def m_bool(value):
    """Transform to a bool if it is not already"""
    if not isinstance(value, bool):
        # check if it is a list
        try:
            value = value[0]
        except TypeError:
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
        elif prop == 'address':
            pass
        elif prop == 'output':
            newprop = '_' + prop
            newprop = getattr(the_class, newprop)
            #newprop = newprop
            pdict.setdefault(prop, newprop)
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

def spacelessify(name):
    """
    remove all special signs
    you can have letters, numbers and dot
    replace space by underscores
    """
    if name is not None:
        # Remove all non-word characters (everything except numbers and letters)
        newname = re.sub(r"[^\w\s\.]", '', name)
        # Replace all runs of whitespace with '_'
        newname = re.sub(r"\s+", '_', newname)
        if not name.startswith('_'):
            if newname.startswith('_'):
                newname = newname[1:]
        if not name.endswith('_'):
            if newname.endswith('_'):
                newname = newname[:-1]
        return newname
    else:
        return name

def set_attributes(the_instance, the_dict):
    """
    set value for attribute
    catch error if needed
    """
    for att, val in the_dict.items():
        # children attribute is for Node Instance
        if att == 'children':
            if the_dict[att]:
                for child in the_dict[att]:
                    the_instance.new_child(child)
        elif att == 'parameter':
            if the_dict[att]:
                the_instance.get_device().new_parameter(val)
        elif att == 'snapshots':
            if the_dict[att]:
                for snap in the_dict[att]:
                    the_instance.snap(snap)
        elif att == 'outputs':
            for protocol, output in val.items():
                for out in output:
                    if protocol == 'OSC':
                        the_instance.new_output(protocol=protocol, **out)
                        if __dbug__:
                            print('import creates an OSC output')
                    if protocol == 'MIDI':
                        the_instance.new_output(protocol=protocol, **out)
                        if __dbug__:
                            print('import creates a MIDI output')
        else:
            try:
                setattr(the_instance, att, val)
            except(AttributeError) as error:
                if __dbug__ == 4:
                    print(str(error) + ' ' + att)
