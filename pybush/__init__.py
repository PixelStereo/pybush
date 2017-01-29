#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package contains useful classes designed to organize your Application.

It allows you to interact with various protocols from/to your app.
For now, only OSC is implemented, but the goal is to support at least :
- OSC
- Minuit
- PJ-Link
- MIDI
- DMX / ARTNET
- Serial

A few apps that might use pybush :
- Configurable Bridge between protocols
- Inter-media sequencer
- IOT embedded app
- Show controler

Don't beat about the bush, it is lib for writing inter/multi-media scenario.

As a bush, pybush model is a tree graph, with one and only one trunk.
A Trunk might conatain branches and leaves.

Trunk Class
This is the first thing to create. The trunk is an entry point to access
branches and leaves.

from pybush import new_trunk

my_app = new_trunk('My App')

Leave Class
Now that we have a trunk, you can create some leaves.

pos_x = my_app.new_parameter('pos/x')

A leave is a Branch with a leaf attributte set to a Leaf Instance

now this is True :

my_app.children[0].children[0].parameter = pos_x

pos_x.name = 'x'

pos_X.parent.name = 'pos'

You cam call make_state() method for each Branch
that makes leaves comming back to a certain state 

Name must be unique in the namespace.
When you create a name, it will raise an error if there is already
the same name.

Nodes are used to organize your namespace.
Leaves are used for parameters and controlers.
- Parameter : It is a string, integer, boolean, float or list with a state.
- Controler : It is the result of a computation (algorythm/remote/controler)

There is others optionnals properties for each branch / state / trunk:
- tags : tags are un unordered list of strings.
- description : description for the object

-------------------------------------------------------------------------------

    Copyright (c) 2015 - 2017 Pixel Stereo

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Changelog:
-------------------------------------------------------------------------------

- v0.1.3 - Jan. 16th 2017
    - Parameters are into a Device, and no more an application

- v0.1.2 - Jan. 15th 2017
    - Add two animations for parameters (ramp and random)

- v0.1.1 - Apr. 6th 2016
    - First draft
"""

from __future__ import print_function
from __future__ import unicode_literals
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__release__ = __version__

from pybush.device import Device
from pybush.constants import __devices__

def new_device(dict_import=None, name=None, tags=None, version=None, author=None):
    """
    Create a new device
        :return node object if successful
        :return False if name is not valid (already exists or is not provided)
    """
    if isinstance(dict_import, dict):
        # we import a python dict to create the child
        device = Device (parent=None, name=dict_import['name'],
                                version=dict_import['version'], author=dict_import['author'], \
                                tags=dict_import['tags'])
    else:
        # if the child argument is only a string, this is the name of the new_child to create
        device = Device(name=name, tags=tags, version=version, author=author)
    if device:
        __devices__.append(device)
        return __devices__[-1]
    else:
        return False

def get_devices():
    """
    return a list of devices
    """
    return __devices__
