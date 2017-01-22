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
from pybush.functions import prop_list
from pybush.output import OutputOSC, OutputMIDI


class Device(Node):
    """
    Device Class represent a fixture, a unit
    Device inherit from Node
    Device Class creates author and version attributes
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
        for att, val in kwargs.items():
            setattr(self, att, val)

    def __repr__(self):
        printer = 'Device (name:{name}, author:{author}, version:{version}, children:{children})'
        return printer.format(name=self.name, author=self.author, \
                                version=self.version, children=self.children)

    @property
    def output(self):
        """
        The port to output this project
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
                print('DO YOU WANT TO CHANGE THE TYPE OF THE OUTPUT FOR THIS DEVICE', self.name)
                raise BushTypeError('Wait for a ' + self.output.protocol + ',  but receive a', out.protocol)
        else:
            raise BushTypeError('Wait for an Output but receive a', out.__class__.__name__)

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
        return {'name':self.name, 'author':self.author, 'version':self.version, \
                'children':child_export, 'outputs':out_export}

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
        return a list of outputs of this project
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
        """return the protocols available for this project"""
        protocols = []
        for out in self.outputs:
            proto = out.protocol
            if not proto in protocols:
                protocols.append(proto)
        if protocols == []:
            return None
        else:
            return protocols

    def new_output(self, protocol="OSC", **kwargs):
        """
        Create a new output for this project
        args:Mandatory argument is the protocol that you want to use for this output
        (OSC, MIDI, serial, ArtNet)
        rtype:Output object
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
            for key, value in kwargs.items():
                setattr(output, key, value)
            self._outputs.append(output)
            return self._outputs[taille]
        else:
            return False

    def new_parameter(self, **kwargs):
        """
        Create a new parameter (node + node.makeparameter())
        """
        pass

    def del_output(self, output):
        """
        delete an output of this project
        """
        if output in self.outputs:
            # delete the output
            self._outputs.remove(output)
        else:
            if __dbug__:
                print("ERROR - trying to delete an output which not exists \
                      in self._outputs", output)

    def new_parameter(self, dict_import={}):
        """
        create a parameter in the device
        name must be provided.
        """
        self._final_node = self
        def create_node():
            if isinstance(toto, str):
                node = self._final_node.new_child(name=toto)
            else:
                node = self._final_node.new_child(name=toto[0])
            self._final_node = node
            if isinstance(toto, str):
                pass
            else:
                toto.pop(0)
            return self._final_node
        lock = False
        if 'name' in dict_import.keys():
            if '/' in dict_import['name']:
                # this is a parameter in a child node of the device
                # we will create nodes first, and then parameter
                toto = dict_import['name'].split('/')
                if self.children:
                    for child in self.children:
                        if child.name == toto[0]:
                            return False
                    # at this point, it seems that 
                    # there is no child with the same name
                    # so please create this node as a child
                while len(toto) > 1:
                    node = create_node()
                    # and create parameters attributes for the node
                dict_import.setdefault('parent', node)
                dict_import.pop('name')
                node._parameter = Parameter(**dict_import)
                lock = node._parameter
            else:
                # it is a root parameter
                toto = dict_import['name']
                node = create_node()
                dict_import.setdefault('parent', node)
                # remove 
                dict_import.pop('name')
                self._parameter = Parameter(**dict_import)
                lock = self._parameter
        if not lock:
            print('there is already a child with the same name', dict_import['name'])
        return lock


    def make_parameter(self, *args, **kwargs):
        """
        Call this method to attach a parameter to this node
        You can send a string or a dict as argument
        string : create a parameter with this name
        """
        if args:
            if self._parameter is None:
                if isinstance(args[0], dict):
                    child = args[0]
                    child.setdefault('parent', self)
                    self._parameter = Parameter(**child)
                else:
                    kwargs.setdefault('parent', self)
                    self._parameter = Parameter(**kwargs)
                return self._parameter
            else:
                return False
        else:
            self._parameter = Parameter(parent=self)
            return self._parameter
