#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Device Class might also be called Fixture Class.
It describe a device, an instrument, a pixel, a bunch of parameters.
A Device has some parameters and/or nodes
A Device has some protocol/plugin for input/output
(you can override device.input/output by provinding parameter.input/output)
"""

from pybush.node import Node
from pybush.constants import __dbug__
from pybush.errors import BushTypeError
from pybush.parameter import Parameter
from pybush.functions import prop_list, set_attributes
from pybush.file import File
from pybush.output import OutputOSC, OutputMIDI


class Device(Node, File):
    """
    Device Class represent a fixture, a unit
    Device inherit from Node
    Device Class creates author and version attributes
    It inherits from File Class. It adds write(), read() functions.
    That export/import json files for any Node with all its chidren
    """
    def __init__(self, **kwargs):
        super(Device, self).__init__(**kwargs)
        self._author = None
        self._version = None
        self._input = None
        self._output = None
        # list of all outputs for this device
        self._outputs = None
        # list of all inputs for this device
        self._inputs = None
        # kwargs setup attributes
        set_attributes(self, kwargs)
        # temporary workaround
        self._final_node = None

    def post_print(self, printer):
        printer = printer[5:]
        printer = 'Device' + printer
        if self.author:
            printer = printer + ' - author :  ' + self.author
        if self.version:
            printer = printer + ' - version :  ' + str(self.version)
        if self.outputs:
            printer = printer + ' - outputs :  ' + str(len(self.outputs))
        if self.children:
            printer = printer + ' - children :  ' + str(len(self.children))
        if self.address:
            printer = printer + ' - address :  ' + self.address
        return printer

    @property
    def output(self):
        """
        The port to output this device
        Initialised to the first output
        """
        if self._output:
            return self._output
        else:
            if self._outputs:
                return self._outputs[0]

    @output.setter
    def output(self, out):
        if 'protocol' in prop_list(out):
            if out.protocol == self.output.protocol:
                self._output = out
            else:
                raise BushTypeError(self.output.protocol, out.protocol)
        else:
            raise BushTypeError('Output', out)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        child_export = None
        if self.children:
            child_export = []
            for child in self.children:
                child_export.append(child.export())
        out_export = None
        if self.outputs:
            out_export = {}
            for proto in self.getprotocols():
                out_export.setdefault(proto, [])
                for out in self.getoutputs(proto):
                    out_export[proto].append(out.export())
        return {
                'name': self.name,
                'author': self.author,
                'version': self.version,
                'children': child_export,
                'outputs': out_export
                }

    # ----------- AUTHOR -------------
    @property
    def author(self):
        """
        Current author of the device
        """
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    # ----------- VERSION -------------
    @property
    def version(self):
        """
        Current version of the device
        """
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def outputs(self):
        """
        return a list of outputs of this device
        """
        return self._outputs

    def getoutputs(self, protocol):
        """
        return a list of available output for this protocol
        """
        if self.outputs:
            outputs = []
            for out in self.outputs:
                if protocol == out.protocol:
                    outputs.append(out)
            return outputs
        else:
            return None

    def getprotocols(self):
        """
        return the protocols available for this device
        """
        protocols = []
        for out in self.outputs:
            proto = out.protocol
            if proto not in protocols:
                protocols.append(proto)
        if protocols == []:
            return None
        else:
            return protocols

    def new_output(self, protocol="OSC", **kwargs):
        """
        Create a new output for this device

            args:
                Mandatory argument is the protocol
                you want to use for this output
                (OSC, MIDI, serial, ArtNet)
            rtype:
                Output object
        """
        if not self._outputs:
            self._outputs = []
        taille = len(self._outputs)
        if protocol == "OSC":
            output = OutputOSC()
        elif protocol == "MIDI":
            output = OutputMIDI()
        else:
            output = None
        if output:
            set_attributes(output, kwargs)
            self._outputs.append(output)
            return self._outputs[taille]
        else:
            return False

    def del_output(self, output):
        """
        delete an output of this device
        """
        if output in self.outputs:
            # delete the output
            self._outputs.remove(output)
        else:
            if __dbug__:
                print("ERROR - trying to delete an output which not exists \
                      in self._outputs", output)

    def new_parameter(self, dict_import):
        """
        create a parameter in the device
        name must be provided.
        """
        self._final_node = self

        def _create_node():
            """
            function to create a node to another node
            """
            if isinstance(the_import, str):
                node = self._final_node.new_child(name=the_import)
            else:
                node = self._final_node.new_child(name=the_import[0])
            self._final_node = node
            if isinstance(the_import, str):
                pass
            else:
                the_import.pop(0)
            return self._final_node

        def _create_parameter(node, param_dict):
            """
            internal method to create a parameter to a node
            """
            param_dict.setdefault('parent', node)
            if 'name' in param_dict.keys():
                param_dict.pop('name')
            node.parameter = Parameter(**param_dict)
            return node.parameter
        lock = None
        if 'name' in dict_import.keys():
            if '/' in dict_import['name']:
                # this is a parameter in a child node of the device
                # we will create nodes first, and then parameter
                if dict_import['name'].startswith('/'):
                    dict_import['name'] = dict_import['name'][1:]
                the_import = dict_import['name'].split('/')
                if self.children:
                    for child in self.children:
                        if child.name == the_import[0]:
                            # the node already exists. be carreful
                            # to not replace it
                            pass
                # at this point, it seems that
                # there is no child with the same name
                # so please create this node as a child
                while len(the_import):
                    node = _create_node()
                    # and create parameters attributes for the node
                lock = _create_parameter(node, dict_import)
            else:
                # it is a root parameter
                the_import = dict_import['name']
                node = _create_node()
                lock = _create_parameter(node, dict_import)
        return lock

    def read(self, filepath):
        """
        Fillin Bush with objects created from a json file

        Creates Outputs obects
        First, dump attributes, then outputs.

        :returns: True if file formatting is correct, False otherwise
        :rtype: boolean
        """
        # self.read is a method from File Class
        device_dict = self.load(filepath)
        # TODO : CHECK IF THIS IS A VALID DEVICE FILE
        # if valid python dict / json file
        if device_dict:
            if __dbug__:
                print('initing device called : ' + filepath)
            self.__init__()
            if __dbug__:
                print('loading device called : ' + filepath)
        else:
            if __dbug__:
                print('ERROR 901 - file provided is not a valid file' + str(filepath))
        try:
            if __dbug__:
                print('--- new-device : ' + device_dict['name'] + ' --- ')
            # iterate each attributes of the selected device
            set_attributes(self, device_dict)
            if __dbug__:
                print('device loaded : ' + str(self.name))
            return True
        # catch error if file is not valid or if file is not a valide node
        except (IOError, ValueError) as error:
            if __dbug__:
                print(error,    "ERROR 902 - device cannot be loaded, \
                                this is not a valid Device")
            return False
