#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application Class is the root class
An application has some leaves and/or nodes
An Application has some protocol/plugin for input/output
"""

from pybush.node import Node
from pybush.functions import prop_dict
from pybush.constants import __dbug__, _applications

def application_new(*args, **kwargs):
    """Create a new application
        :return node object if successful
        :return False if name is not valid (already exists or is not provided)"""
    size = len(_applications)
    _applications.append(Application(args[0]))
    for key, value in kwargs.items():
        setattr(_applications[size], key, value)
    return _applications[size]

def applications():
    """return a list of applications"""
    return _applications

def applications_export():
    """Export Applications"""
    apps = {'applications':{}}
    for app in applications():
        apps['applications'].setdefault(app.name, {'attributes': \
            {'author':app.author, 'name':app.name, 'version':app.version}})
        if app.nodes:
            apps['applications'][app.name].setdefault('nodes', {})
            for node in app.nodes:
                apps['applications'][app.name]['nodes'].setdefault(node.name, prop_dict(node))
    return apps


class Application(Node):
    """Application Class"""
    def __init__(self, name):
        super(Application, self).__init__(name)
        self._author = 'unknown'
        self._version = 'unknown'
        self._name = name

    def __repr__(self):
        printer = 'Application (name:{name}, author:{author}, version:{version})'
        return printer.format(name=self.name, author=self.author, version=self.version)

    # ----------- AUTHOR -------------
    @property
    def author(self):
        "Current author of the application"
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
    @author.deleter
    def author(self):
        return False

    # ----------- VERSION -------------
    @property
    def version(self):
        "Current version of the application"
        return self._version
    @version.setter
    def version(self, version):
        self._version = version
    @version.deleter
    def version(self):
        return False
