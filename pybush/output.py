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
    def __init__(self, name='Untitled Output', description='Description of a Untitled Output', parent=None, port=None):
        super(Output, self).__init__(name=name, description=description, parent=parent)
        self._port = port

    @property
    def protocol(self):
        """
        Protocol property is used to navigate between outputs
        """
        return self._protocol

    @property
    def port(self):
        """
        A port contains all informations need to sent a message to this output
        """
        return self._port
    @port.setter
    def port(self, port):
        self._port = port

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        # must be sub-classed
        pass

class OutputMIDI(Output):
    """
    Creates an output port for Midi Device.
    A Midi Device can handle all type of Midi messages
    """
    def __init__(self, name='Midi Output', parent=None, port=None, channel=1, message='CC'):
        super(OutputMIDI, self).__init__(name=name, parent=parent, port=port)
        self._protocol = 'MIDI'
        self._channel = channel
        self._message = message

    @property
    def channel(self):
        """
        The MIDI Channel used to send out the message
        """
        return self._channel
    @channel.setter
    def channel(self, value):
        flag = False
        if isinstance(value, int):
            if value > 0 and value < 17:
                flag = True
        if flag:
            self._channel = value
            return True
        else:
            return False


    def export(self):
        return {'name':self.name, 'port':self.port,'channel':self.channel}

class OutputOSC(Output):
    """
    OutputUdp is a based class for all UDP based output
    You can use it if you want to send raw UDP.
    If you want to send OSC through UDP, please use OutputOsc as it checks if your OSC messages
    are correctly formatted.
    We might create a new class : OutputOsc as a subclass of OutputUdp.
    It should be used to double check that you send a correct OSC format message/bundle.
    """
    def __init__(self, name='OSC Output', parent=None, port='127.0.0.1:1234'):
        super(OutputOSC, self).__init__(name=name, parent=parent, port=port)
        if not self.name:
            self.name = 'Untitled Udp Output'
        self._protocol = 'OSC'

    def __repr__(self):
        printer = 'OSC Output (name:{name}, port:{port})'
        return printer.format(name=self.name, port=self.port)

    def export(self):
        return {'name':self.name, 'port':self.port}
