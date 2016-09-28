#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
File Class hosts services for file loading/writing
"""
import os
import simplejson as json
from pybush.functions import prop_dict, iterate_dict
from pybush.constants import __dbug__, _devices, _file_extention


def get_file_extention():
    """return the file extention"""
    file_extention = '.' + _file_extention
    return file_extention


class File(object):
    """docstring for File"""
    def __init__(self, name, parent, tags=None, priority=None, path=None):
        super(File, self).__init__()
        self._path = path
        self._parent = parent

    def reset(self):
        """
        Must be override by children
        """
        pass

    def export(self):
        """
        Must be override by children
        """
        #self._parent.export()
        pass
        
    @property
    def path(self):
        """
        This is the filepath where to write the file or where it is located.
        It's initialised at None when created, and can be set to any valid path.

        :param path: valid filepath. Return True if valid, False otherwise.
        :type path: string
        """
        return self._path
    @path.setter
    def path(self, value):
        self._path = value

    def read(self, path):
        """
        Read a Node file from hard drive. Must be valid.
        if valid it will be loaded and return True, otherwise, it will return False

            :param path: Filepath to read from.
            :type path: string
            :returns: Boolean
            :rtype: True if the node has been correctly loaded, False otherwise
        """
        path = os.path.abspath(path)
        if not os.path.exists(path):
            print("ERROR 901 - THIS PATH IS NOT VALID " + path)
            return False
        else:
            print("loading JSON from " + path)
            if self.load(path):
                self._path = path
                self.write(path)
                return True
            else:
                return False

    def load(self, path):
        """
        Load a Node from a file from hard drive
        It will play the file after loading, according to autoplay attribute value

            :arg: file to load. Filepath must be valid when provided, it must be checked before.

            :rtype:True if the node has been correctly loaded, False otherwise
        """
        flag = False
        try:
            with open(path) as in_file:
                # clear the node
                loaded = json.load(in_file)
                flag = True
        # catch error if file is not valid or if file is not a Node file
        except (IOError, ValueError):
            print("ERROR 906 - node not loaded, this is not a valid Node file")
            return False
        if flag:
            # create objects from loaded file
            flag = self.fillin(loaded)
        return flag

    def fillin(self, loaded):
        """
        Creates Outputs, Scenario and Events obects
        First, dump attributes, then outputs, scenario and finish with events.

        :returns: True if file formatting is correct, False otherwise
        :rtype: boolean
        """
        try:
            # reset node
            self.reset()
            # dump attributes
            print('-------------------')
            print('-------------------')
            print(loaded)
            print('-------------------')
            print('-------------------')
            loaded = iterate_dict(loaded)
            if loaded == True:
                loaded = {}
            if loaded == {}:
                # node has been loaded, lastopened date changed
                # we have a path because we loaded a file from somewhere
                print("node loaded")
                return True
            else:
                print('ERROR 906 - loaded node file has not been totally loaded', loaded)

                return False
        # catch error if file is not valid or if file is not a valide node
        except (IOError, ValueError) as Error:
            if debug:
                print(Error, "ERROR 907 - node not loaded, this is not a valid Node")
            return False

    def write(self, path=None):
        """
        Save a Node to a JSON textfile
        """
        if path:
            savepath = path
            self._path = path
        else:
            savepath = self._path
        if savepath:
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
            return False


