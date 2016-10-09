#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
File Class is an abstract class to add read/write json files
"""
import os

from pybush.constants import __dbug__, __file_extention__
from pybush.functions import load_json

def file_extention():
    """return the file extention"""
    file_extention = '.' + __file_extention__
    return file_extention

class File(object):
    """
    Abstract class
    Implements read and write methods
    Implements path attribute
    Instance must have import / export / reset methods
    Instance must have name attribute
    """
    def __init__(self, name, path=None):
        super(File, self).__init__(name)
        self._path = path
        self.name = name

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path


    def load(self, path):
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
            if __dbug__:
                print("ERROR 901 - THIS PATH IS NOT VALID " + path)
            return False
        else:
            if __dbug__:
                print("--- loading JSON from " + path)
            loading = load_json(path)
            if loading:
                # register the path for the current load
                self.path = path
                if __dbug__:
                    print("--- succesfull JSON loading from " + path)
                return loading
            else:
                if __dbug__:
                    print("--- problem when loading JSON from " + path + ' - Maybe your file was empty ? ?')
                return False
