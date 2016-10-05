#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
File Class hosts services for file loading/writing
"""
import os
import simplejson as json
from pybush.functions import prop_dict
#from pybush.device import device_new
from pybush.constants import __dbug__, _devices, _file_extention


def get_file_extention():
    """return the file extention"""
    file_extention = '.' + _file_extention
    return file_extention

def load_json(path):
    """
    Load a Node from a file from hard drive
    It will play the file after loading, according to autoplay attribute value

        :arg: file to load. Filepath must be valid when provided, it must be checked before.

        :rtype:True if the node has been correctly loaded, False otherwise
    """
    content = False
    try:
        with open(path) as in_file:
            # clear the node
            content = json.load(in_file)
    # catch error if file is not valid or if file is not a Node file
    except (IOError, ValueError):
        print("ERROR 906 - node not loaded, this is not a valid Node file")
        return False
    return content

def load(path):
    """
    Read a Node file from hard drive. Must be valid.
    if valid it will be loaded and return True, otherwise, it will return False

        :param path: Filepath to read from.
        :type path: string
        :returns: Boolean
        :rtype: True if the node has been correctly loaded, False otherwise
    """
    path = os.path.abspath(path)# + get_file_extention()
    if not os.path.exists(path):
        print("ERROR 901 - THIS PATH IS NOT VALID " + path)
        return False
    else:
        print("loading JSON from " + path)
        loading = load_json(path)
        if loading:
            write(path)
            return loading
        else:
            return False
