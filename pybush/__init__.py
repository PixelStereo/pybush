#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package contains useful classes designed to organize your Application
It allows you to interact with various protocols from/to your app
It works as a project manager for writing inter/multi-media scenario.

As a bush, pybush model is a tree graph, with branches and leaves.

Here everything is based on the Node base Class.

The 'root' Node is a class called Application.
The application is an entry to acces its children or its sibling through different protocols
In your application, you can create any nodes or directly any parameters you want.

In each Node, you can create another nodes.
Each Node can contain a value. If it does, it is a Parameter.
It is just a Node with a value (and attributes relative to the value)
When you create a parameter, it automatically creates a node, as it is bassed on the Node Class.
So you can even create another node or another parameter under a node

Node base class has at least 1 property which is a name.

Name must be unique in the namespace.
When you create a name, it will raise an error if there is already the same name.

Nodes are used to organize your namespace.
Leaves are used for parameters, messages and returns.
- Parameter : It is a string, integer, boolean, float or list with a state.
- Message : It is a message is as a parameter but without a state.
- Return : It is a return is a result of a computation made by an algorythm or a controller.

There is others optionnals properties for each nodes, which are :
- tags : tags are un unordered list of strings.


-------------------------------------------------------------------------------

    Copyright (c) 2015 - 2016 Pixel Stereo

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Changelog:
-------------------------------------------------------------------------------

- v0.1.1 - Apr. 6th 2016
    - First draft

"""
from __future__ import print_function
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__release__ = __version__

try:
    str = unicode
    def is_string(test):
        """
    	Fonction used for both python 2 and 3
    	"""
        return isinstance(test, basestring)
except NameError:
    def is_string(test):
        """
    	Fonction used for both python 2 and 3
    	"""
        return isinstance(test, str)
