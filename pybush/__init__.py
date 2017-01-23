#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package contains useful classes designed to organize your Application
It allows you to interact with various protocols from/to your app
It works as a project manager for writing inter/multi-media scenario.

As a bush, pybush model is a tree graph, with branches and leaves.

Here everything is based on a Node concept
We have an abstract base Class : NodeAbstract

The 'root' Node is a class called Device.
This is the first thing to create.
The device is an entry to acces its children or its sibling (both parameters)
through different protocols. In your application, you can create any nodes
or directly any parameters you want.

In each Node, you can create another nodes.
Each Node can contain a value. If it does, it is a Parameter.
It is just a Node with a value (and attributes relative to the value)
When you create a parameter, it automatically creates a node, as it is bassed
on the Node Class.
So you can even create another node or another parameter under a node

Node base class has at least 1 property which is a name.

Name must be unique in the namespace.
When you create a name, it will raise an error if there is already
the same name.
Nodes are used to organize your namespace.
Leaves are used for parameters and controlers.
- Parameter : It is a string, integer, boolean, float or list with a state.
- Controler : It is the result of a computation (algorythm/remote/controler)

There is others optionnals properties for each nodes, which are :
- tags : tags are un unordered list of strings.


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
        # be careful about children and parameter
        # which needs to instanciate Classes Node and Parameter
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
