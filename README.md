# pybush
[![Coverage Status](https://coveralls.io/repos/github/PixelStereo/pybush/badge.svg?branch=master&bust=1)](https://coveralls.io/github/PixelStereo/pybush?branch=master)
[![Build Status](https://travis-ci.org/PixelStereo/pybush.svg?branch=master)](https://travis-ci.org/PixelStereo/pybush)

=====
####Python Modular framework for real-time inter-media applications

**pybush** can be defined as a framework for creating applications for real-time intermedia
that can be easily accessed through OSC (Open Sound Control) messages, and other protocols later on.

It offers a way to organise your application hierarchicaly based on a tree graph.
Every part of the application inherit from the Node base Class.

For the moment, **pybush** is will be capable of:
-  Creating application with parameters organised hierarchicaly
-  ~~Navigate and access your app through OSC protocol~~
-  Create dynamic scenario and events
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
The tests.py contains a nice exemple to understand what you can do with pybush package.

####Development
---
Development is made on OSX with python 2.7.11    
Continious integration is made on linux for python 2 and 3.
