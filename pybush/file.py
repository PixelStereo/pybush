#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
File Class is an abstract class to add read/write json files
"""
import os
import simplejson as json
from pybush.constants import __dbug__,  __file_extention__
from pybush.functions import load_json


class File(object):
    """
    Abstract class
    Implements read and write methods
    Implements path attribute
    Instance must have import / export / reset methods
    Instance must have name attribute
    """
    def __init__(self, name=None, path=None):
        super(File, self).__init__()
        self._path = path

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    @property
    def file_extention(self):
        """return the file extention"""
        file_extention = '.' + __file_extention__
        return file_extention
    @file_extention.setter
    def file_extention(self, new_f_e_):
        __file_extention__ = new_f_e_

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

    def write(self, savepath=None):
        """
        Write a node on the hard drive.
        """
        if savepath:
            if savepath.endswith("/"):
                savepath = savepath + self.name
            # make sure we will write a file with json extension
            if not savepath.endswith(self.file_extention):
                savepath = savepath + self.file_extention
            try:
                # create / open the file
                out_file = open((savepath), "wb")
            except IOError:
                # path does not exists
                print("ERROR 909 - path is not valid, could not save the node - " + savepath)
                return False
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            print(self.export())
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            print('-----xxxxxxx-x--------')
            try:
                the_dump = json.dumps(self.export(), sort_keys=True, indent=4,\
                                      ensure_ascii=False).encode("utf8")
            except TypeError as error:
                print('ERROR 98 ' + str(error))
                return False
            try:
                out_file.write(the_dump)
                print("file has been written in " + savepath)
                out_file.close()
                return True
            except TypeError as error:
                print('ERROR 99 ' + str(error))
                return False
        else:
            print('no filepath. Where do you want I save the node?')
            return False
