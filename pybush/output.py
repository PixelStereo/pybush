#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements output for scenario-events
An ouput is an object that can send-out commands.
Maybe we might use some plug in pybush to have in/out access for a bunch of nodes (pybush / a bush)
"""

from pybush.node_abstract import NodeAbstract


class Output(NodeAbstract):
    """
    Abstract class
    Create a new output for a device

    """
    def __init__(self, name=None, description=None, parent=None, port=None):
        super(Output, self).__init__(name=name, description=description, parent=parent)
        self._port = port
        if not self.name:
            self.name = 'Untitled Output'
        if not self.description:
            self.description = "I'm an output"

    @property
    def protocol(self):
        return self._protocol

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, port):
        self._port = port


class OutputMIDI(Output):
    """
    Creates an output port for Midi Device.
    A Midi Device can handle all type of Midi messages
    """
    def __init__(self, name=None, parent=None, port=None):
        super(OutputMIDI, self).__init__(name=name, parent=parent, port=port)
        if not self.name:
            self.name = 'Untitled Midi Output'
        self._protocol = 'MIDI'

class OutputOSC(Output):
    """
    OutputUdp is a based class for all UDP based output
    You can use it if you want to send raw UDP.
    If you want to send OSC through UDP, please use OutputOsc as it checks if your OSC messages
    are correctly formatted.
    We might create a new class : OutputOsc as a subclass of OutputUdp.
    It should be used to double check that you send a correct OSC format message/bundle.
    """
    def __init__(self, name=None, parent=None, port='127.0.0.1:1234'):
        super(OutputOSC, self).__init__(parent=parent, port=port)
        if not self.name:
            self.name = 'Untitled Udp Output'
        self._protocol = 'OSC'

    def __repr__(self):
        printer = 'OSC Output (name:{name}, port:{port})'
        return printer.format(name=self.name, port=self.port)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        return {'name':self.name, 'protocol':self.protocol, 'port':self.port}
