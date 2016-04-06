# pybush
=====
####Python Modular framework for real-time inter-media applications
---
**This is an alpha version - Do not use it for production, because API must changes a lot before release**
---

**pybush** can be defined as a framework for creating applications for real-time intermedia
that can be easily accessed through OSC (Open Sound Control) messages.
It offers a way to organise your application hierarchicaly and creating events and scenario.

For the moment, **pybush** is will be capable of:

-  Creating application with parameters organised hierarchicaly
-  ~~Navigate and access your app through OSC protocol~~
-  Create dynamic scenario and events
-  Save projects to json files

####QuickStart
---
The tests.py contains a nice exemple to understand what you can do with pybush package.

####Development
---
Development is made on OSX with python 2.7.11    
Continious integration is made on linux for python 2 and 3.

[![Code Climate](https://codeclimate.com/github/PixelStereo/pybush/badges/gpa.svg)](https://codeclimate.com/github/PixelStereo/pybush)
[![Coverage Status](https://coveralls.io/repos/github/PixelStereo/pybush/badge.svg?branch=master)](https://coveralls.io/github/PixelStereo/pybush?branch=master)
[![Issue Count](https://codeclimate.com/github/PixelStereo/pybush/badges/issue_count.svg)](https://codeclimate.com/github/PixelStereo/pybush)
[![Build Status](https://travis-ci.org/PixelStereo/pybush.svg?branch=master)](https://travis-ci.org/PixelStereo/pybush)

####Documentation
---
Documentation is available online [on this page](http://pixelstereo.github.io/pybush)    

If you need/want to build the documentation from the repo, here are the steps : 

    pip install sphinx
    cd docs/source
    make html

####Roadmap
---
#####0.1 - Dec. 2015 -> March. 2016
* ~~Scenario and events sends OSC commands~~
* ~~multiple projects architecture~~
* ~~Python 2 and 3 compatibility~~
* ~~Unit tests and Continious integration~~
* ~~Nice and solid UTF8 Encoding everywhere~~
* ~~project-related commands (auto-play)~~
* ~~Loop for project / scenario / event~~
* Scenario behavior creates nice sequence (aka auto-cue / auto-follow)

#####0.2 - Apr. 2016 -> June. 2016
* OSC server for projects, scenario and events access
* OSC listening creates Nodes, Models and Parameters
* Namespace implementation for automagic events creation
* Minuit implementation

#####0.3 - Jul. 2016 -> Dec. 2017
* Graphic display of projects, scenario and events
* Random generator
* Artnet and MIDI in/out
