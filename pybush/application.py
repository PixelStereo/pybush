#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
application Class is the root class
A application has some parameters and/or nodes
A application has some protocol/plugin for input/output
"""

from pybush.node import Node
from pybush.constants import __dbug__
from pybush.errors import LektureTypeError
from pybush.output import OutputOSC, OutputMIDI


class Application(Node):
    """
    Application Class represent a application
    Application inherit froù Node
    Application Class creates author and version attributes
    """
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self._author = None
        self._version = None
        self._output = None
        # list of all outputs for this application
        self._outputs = None
        # kwargs setup attributes
        for att, val in kwargs.items():
            setattr(self, att, val)

    def __repr__(self):
        printer = 'Application (name:{name}, author:{author}, version:{version}, children:{children})'
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
        if out.protocol == self.protocol:
            self._output = out
        else:
            print('DO YOU WANT TO CHANGE THE TYPE OF THE OUTPUT FOR THIS DEVICE', self.name)
            raise LektureTypeError('Wait for an Output but receive a', out.protocol)

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
        Current author of the application
        """
        return self._author
    @author.setter
    def author(self, author):
        self._author = author

    # ----------- VERSION -------------
    @property
    def version(self):
        """
        Current version of the application
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
