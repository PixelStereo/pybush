#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Animation's library
"""

import multiprocessing
from time import time
from random import uniform

CURRENT_TIME = lambda: time() * 1000


class Automation(multiprocessing.Process):
    """
    This is an abstact class for an Automation
    You can automate parameter in this way :
    - update parameter.value
    - parameter.ramp(destination=1, duration=1000, grain=10) update parameter.value each 10 ms if grain == 10
    - parameter.random(destination=1, duration=1000, grain=10)

    A Player that play things
    """
    def __init__(self, parent, value=0, destination=1, duration=1000, grain=10):
        super(Automation, self).__init__()
        self.parent = parent
        self.value = value
        self.destination = destination
        self.duration = duration
        self.grain = grain
        self.start()


class RampGenerator(Automation):
    """
    Instanciate a thread for Playing a ramp
    step every 10 ms
    Allow to do several ramps in a same device / scenario / event
    :param target:
    """
    def __init__(self, parent, origin, destination, duration, grain):
        super(RampGenerator, self).__init__(parent, origin, destination, duration, grain)

    def run(self):
        for step in self.ramp():
            self.parent.value = step

    def ramp(self):
        """
        linear interpolation from a value to another in a certain time
        """
        start = CURRENT_TIME()
        last = start
        step = float( (self.destination - self.value) / ( float(self.duration / self.grain) ))
        while (CURRENT_TIME() < (start + self.duration)):
            while (CURRENT_TIME() < last + self.grain):
                pass # wait
            last = CURRENT_TIME()
            self.value += step
            yield self.value


class RandomGenerator(Automation):
    """
    Instanciate a thread for Playing a ramp

    step every 10 ms

    Allow to do several ramps in a same device / scenario / event

    :param target:
    """
    def __init__(self, parent, origin, destination, duration, grain):
        super(RandomGenerator, self).__init__(parent, origin, destination, duration, grain)

    def run(self):
        for step in self.random():
            self.parent.value = step
        self.parent.value = self.destination

    def random(self):
        """
        Generate pseudo-random values in a certain range during a certain time
        """
        start = CURRENT_TIME()
        last = start
        while (CURRENT_TIME() < (start + self.duration)):
            while (CURRENT_TIME() < last + self.grain):
                pass # wait
            last = CURRENT_TIME()
            origin = uniform(self.parent.domain[0], self.parent.domain[1])
            yield origin
