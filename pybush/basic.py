#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Basic Class
"""
from pybush.constants import __dbug__
from pybush.functions import set_attributes


class Basic(object):
    """
    Basic Class
    """
    def __init__(self, **kwargs):
        super(Basic, self).__init__()
        # this is not really clean.
        if 'children' in kwargs.keys():
            kwargs.pop('children')
        # initialise attributes/properties of this node
        self._description = None
        self._tags = []
        self._name = None
        # kwargs setup attributes
        set_attributes(self, kwargs)

    def __repr__(self):
        printer = '(name:{name}, '
        'description:{description}, '
        'tags:{tags})'
        printer = self.post_print(printer)
        return printer.format(  name=self.name,
                                description=self.description, \
                                tags=self.tags)

    @property
    def name(self):
        """
        name of the node
        """
        return self._name
    @name.setter
    def name(self, name):
        if name:
            '_'.join([i if ord(i) < 128 else ' ' for i in name])
            name = name.replace(" ", "_")
        self._name = name

    @property
    def description(self):
        """
        Description of this node
        You could here send a few words explainig this node.

        :Args:String
        :Returns:String
        """
        return str(self._description)
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def tags(self):
        """
        Current tags of the node
        """
        return self._tags
    @tags.setter
    def tags(self, tags):
        self._tags = tags

    def add_tag(self, tag):
        """
        add a tag to this node
        """
        if tag in self._tags:
            if __dbug__ >= 3:
                print('already in')
        else:
            self._tags.append(tag)

    def del_tag(self, tag):
        """
        del a tag for this node
        """
        if tag in self._tags:
            self._tags.remove(tag)
        else:
            if __dbug__ >= 3:
                print('not in')
    @property
    def service(self):
        """
        Return the service of the node
        """
        return self.__class__.__name__

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        basic = {}
        basic.setdefault('name', self.name)
        basic.setdefault('description', self.description)
        basic.setdefault('tags', self.tags)
        basic = self.post_export(basic)
        return basic

    def post_export(self, something):
        """
        might be subclassed
        """
        pass

    def post_print(self, printer):
        """
        must be subclassed
        """
        printer = 'Basic' + printer
        return printer

    def reset(self):
        """
        Clear the content of the node
        """
        pass
