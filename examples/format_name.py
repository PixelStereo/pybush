#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
lib_path = os.path.abspath('./../')
sys.path.append(lib_path)

from pybush.functions import spacelessify


name = ' no na )- ) à î Ö ^ me '
other_name = " I can't get no satisfaction! "
print(spacelessify(name))
print(spacelessify(other_name))
