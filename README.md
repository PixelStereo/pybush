# pybush
[![Codacy Badge](https://api.codacy.com/project/badge/grade/f17bbb174ef24686824a4f9142b36e83)](https://www.codacy.com/app/contact_37/pybush)
[![Build Status](https://travis-ci.org/PixelStereo/pybush.svg?branch=master)](https://travis-ci.org/PixelStereo/pybush)
[![Codacy Badge](https://api.codacy.com/project/badge/coverage/f17bbb174ef24686824a4f9142b36e83)](https://www.codacy.com/app/contact_37/pybush)
[![Code Climate](https://codeclimate.com/github/PixelStereo/pybush/badges/gpa.svg)](https://codeclimate.com/github/PixelStereo/pybush)
[![Issue Count](https://codeclimate.com/github/PixelStereo/pybush/badges/issue_count.svg)](https://codeclimate.com/github/PixelStereo/pybush)
[![Code Health](https://landscape.io/github/PixelStereo/pybush/master/landscape.svg?style=flat)](https://landscape.io/github/PixelStereo/pybush/master) 
=====
####Python Modular framework for real-time OSC applications

**pybush** can be defined as a framework for creating applications that can be easily accessed through OSC (Open Sound Control) messages.

It offers a way to organise your application hierarchicaly based on a tree graph.
Every part of the application inherit from the Node base Class.

For the moment, **pybush** is will be capable of:
-  Creating application with parameters organised hierarchicaly
-  ~~Navigate and access your app through OSC protocol~~
-  Save projects to json files


####Documentation
---
Documentation is available online [on this page](http://pixelstereo.github.io/pybush)    

If you need/want to build the documentation from the repo, here are the steps : 

    pip install sphinx
    cd docs/source
    make html

####QuickStart
---
The example/demo.py contains a nice exemple to understand what you can do with pybush package.

####Development
---
Development is made on OSX with python 2.7    
Continious integration is made on linux for python 2.7 / 3.5 / 3.6 / 3.7
