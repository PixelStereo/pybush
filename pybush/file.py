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

def write(path=None):
    """
    Save a Node to a JSON textfile
    """
    pass
    """if savepath:
        if savepath.endswith("/"):
            savepath = savepath + self.name
        # make sure we will write a file with json extension
        if not savepath.endswith(get_file_extention()):
            savepath = savepath + '.'+_file_extention
        try:
            # create / open the file
            out_file = open((savepath), "wb")
        except IOError:
            # path does not exists
            print("ERROR 909 - path is not valid, could not save node - " + savepath)
            return False
        node_string = self.export()
        try:
            the_dump = json.dumps(node_string, sort_keys=True, indent=4,\
                                  ensure_ascii=False).encode("utf8")
        except TypeError as Error:
            print('ERROR 98 ' + str(Error))
            return False
        try:
            out_file.write(the_dump)
            print("file has been written in " + savepath)
            out_file.close()
            return True
        except TypeError as Error:
            print('ERROR 99 ' + str(Error))
            return False
    else:
        print('no filepath. Where do you want I save the node_string?')
        return False"""
