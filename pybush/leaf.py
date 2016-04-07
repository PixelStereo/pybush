
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
A leaf is a node, but without children.
So a Leaf inherit from Node Class
"""

from pybush.node import Node
from pybush.functions import *
from pybush.constants import __dbug__


class Parameter(Node):
	def __init__(self, *args, **kwargs):
		"""ERROR NEED TO SEND ARGS TO NODE. 
		E.G. : IF I DEFINE A PRIORITY OR TAG WHEN CREATING PARAMETER, 
		IT NEED TO BE SEND TO THE NODE"""
		Node.__init__(self,args[0])
		if 'value' in kwargs:
			self.value = kwargs['value']
		else:
			self.value = None
		if 'rangeClipmode' in kwargs:
			self.clipmode = kwargs['clipmode']
		else:
			self.clipmode = None
		if 'domain' in kwargs:
			self.domain = kwargs['domain']
		else:
			self.domain = None
		if 'repetitionsFilter' in kwargs:
			self.repetitions = kwargs['repetitions']
		else:
			self.repetitions = 0
		if 'datatype' in kwargs:
			self.datatype = kwargs['datatype']
		else:
			self.datatype = 'generic'
		if __dbug__:
			print ("........... PARAM %s inited ..........." %args[0])

	def __repr__(self):
		"""represents the parameter class"""
		printer = 'Parameter (name:{name}, value:{value}, datatype:{datatype}, domain:{domain}, clipmode:{clipmode}, repetitions:{repetitions}, priority:{priority}, tags:{tags})'
		return printer.format(name=self.name, value=self.value, datatype=self.datatype, \
        					  domain=self.domain, clipmode=self.clipmode, repetitions=self.repetitions, \
        					  priority=self.priority, tags=self.tags)

	# ----------- RAW VALUE -------------
	@property
	def raw(self):
		"raw value without rangeClipmode or rangeBoundsneither than datatype"
		return self._value

	# ----------- VALUE -------------
	@property
	def value(self):
		"Current value of the parameter"
		if self.datatype == 'decimal':
			value = float(self._value)
			value = m_clip(self,value)
		elif self.datatype == 'string':
			value = str(self._value)
		elif self.datatype == 'integer':
			value = int(self._value)
		return value
	@value.setter
	def value(self, value):
		self._value = value
	@value.deleter
	def value(self):
		pass

	# ----------- DOMAIN -------------
	@property
	def domain(self):
		"Current domain of the parameter"
		return self._domain
	@domain.setter
	def domain(self, domain):
		self._domain = domain
	@domain.deleter
	def domain(self):
		pass

	# ----------- CLIPMODE -------------
	@property
	def clipmode(self):
		"Current clipmode of the parameter"
		return self._clipmode
	@clipmode.setter
	def clipmode(self, clipmode):
		self._clipmode = clipmode
	@clipmode.deleter
	def clipmode(self):
		pass

	# ----------- REPETITIONS -------------
	@property
	def repetitions(self):
		"Current repetitionsFilter of the parameter"
		return self._repetitions
	@repetitions.setter
	def repetitions(self, repetitions):
		self._repetitions = repetitions
	@repetitions.deleter
	def repetitions(self):
		pass

	# ----------- DATATYPE -------------
	@property
	def datatype(self):
		"Current value of the parameter"
		return self.__datatype
	@datatype.setter
	def datatype(self, datatype):
		self.__datatype = datatype
	@datatype.deleter
	def datatype(self):
		pass
