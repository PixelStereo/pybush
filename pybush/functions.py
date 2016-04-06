#! /usr/bin/env python
# -*- coding: utf-8 -*-

def m_clip(int_or_float, value):
	"""clip a value to its domain according to its clipmode
		:return cliped value"""
	if int_or_float.clipmode == 'low' or int_or_float.clipmode == 'both':
		if value < int_or_float.domain[0]:
			value = int_or_float.domain[0]
	if int_or_float.clipmode == 'high' or int_or_float.clipmode == 'both':
		if value > int_or_float.domain[1]:
			value = int_or_float.domain[1]
	return value

def m_bool(value):
	"""Transform to a bool if it is not already"""
	if type(value) != bool:
		try :
			value = value[0]
		except:
			pass
		if value :
			value = True
		else:
			value = False
	return value

def m_int(value):
	"""
	transform a list or string into an integer, if 
	"""
	if isinstance(value, list):
		value = int(value[0])
	elif not isinstance(value, int):
		value = int(value)
	return value

def m_string(value):
	"""transform to a string"""
	if isinstance(value, int) or isinstance(value, float):
		value = str(value)
	elif isinstance(value, list):
		value = str(value[0])
	return value

def prop_list(the_class):
    """
    Make a list of properties presents in a class

    Args:
        an object that is an instance of a class.
        We will check what properties exists for this class

    Returns:
        A list with all properties
        
    Raises:
        Error: Not already implemented
    """
    return [p for p in dir(the_class.__class__) if isinstance(getattr(the_class.__class__, p), property)]

def prop_dict(the_class):
    """
    Make a dict of properties presents in a class, with their values

    Args:
        an object that is an instance of a class.
        We will check what properties exists for this class

    Returns:
        A dict with all properties and their values

    Raises:
        Error: Not already implemented
    """
    plist = prop_list(the_class)
    pdict = {}
    for prop in plist:
        pdict.setdefault(prop, getattr(the_class, prop))
    return pdict
