#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements output for scenario-events
An ouput is an object that can send-out commands.
Maybe we might use some plug in pybush
to have in/out access for a bunch of nodes (pybush / a bush)
"""

from pybush.basic import Basic
from pybush.constants import __dbug__
from pybush.functions import set_attributes


class Output(Basic):
    """
    Abstract class
    Create a new output for a device

    """
    def __init__(self, **kwargs):
        super(Output, self).__init__()
        self._port = None
        set_attributes(self, kwargs)

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
    def __init__(self, **kwargs):
        super(OutputMIDI, self).__init__()
        if __dbug__:
            print('------- creating a MIDI output-------')
        self._protocol = 'MIDI'
        self._channel = 1
        self._message = 'CC'

    def __repr__(self):
        printer = 'MIDI Output (name:{name}, port:{port}, \
                                channel:{channel}, message:{message})'
        return printer.format(name=self.name, port=self.port, \
                                channel=self.channel, message=self.message)

    def export(self):
        return {'name':self.name, 'port':self.port,'channel':self.channel, \
                'message':self.message}

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

    @property
    def message(self):
        """
        The MIDI message
        CONTROL
        NOTE
        PGM
        """
        return self._message
    @message.setter
    def message(self, value):
        if value == 'CONTROL' or value == 'NOTE' or value == 'PGM':
            self._message = value
            return True
        else:
            return False


class OutputOSC(Output):
    """
    OutputUdp is a based class for all UDP based output
    You can use it if you want to send raw UDP.
    If you want to send OSC through UDP, please use OutputOsc
    as it checks if your OSC messages are correctly formatted.
    We might create a new class : OutputOsc as a subclass of OutputUdp.
    It should be used to double check
    that you send a correct OSC format message/bundle.
    """
    def __init__(self, **kwargs):
        super(OutputOSC, self).__init__()
        if __dbug__:
            print('------- creating an OSC output-------')
        self._protocol = 'OSC'
        self._name = 'OSC Output'
        self._port='127.0.0.1:1234'
        set_attributes(self, kwargs)


    def __repr__(self):
        printer = 'OSC Output (name:{name}, port:{port})'
        return printer.format(name=self.name, port=self.port)

    def export(self):
        return {'name':self.name, 'port':self.port}
