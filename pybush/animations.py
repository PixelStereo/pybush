#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Animation's library
"""

import threading
from time import time
from random import uniform

current_milli_time = lambda: time() * 1000


class RandomPlayer(threading.Thread):
    """
    A Player that play things
    """
    def __init__(self, parent, value, destination, duration, grain):
        super(RandomPlayer, self).__init__()
        self.parent = parent
        self.value = value
        self.destination = destination
        self.duration = duration
        self.grain = grain
        self.start()

    def run(self):
        random = Random(self.parent, self.parent.value, self.destination, self.duration, self.grain)
        if random:
            random.join()

    def stop(self):
        """
        Stop the current aanimation
        """
        pass

class RampPlayer(threading.Thread):
    """
    A Player that play things
    """
    def __init__(self, parent, value, destination, duration, grain):
        super(RampPlayer, self).__init__()
        self.parent = parent
        self.value = value
        self.destination = destination
        self.duration = duration
        self.grain = grain
        self.start()

    def run(self):
        ramp = Ramp(self.parent, self.parent.value, self.destination, self.duration, self.grain)
        if ramp:
            ramp.join()

    def stop(self):
        """
        Stop the current aanimation
        """
        pass


class Ramp(threading.Thread):
    """
    Instanciate a thread for Playing a ramp
    step every 10 ms
    Allow to do several ramps in a same project / scenario / event
    :param target:
    """
    def __init__(self, parent, origin=0, destination=1, duration=1000, grain=10):
        super(Ramp, self).__init__()
        self.parent = parent
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.grain = grain
        self.start()

    def run(self):
        for step in self.ramp():
            self.parent.value = step

    def ramp(self):
        """
        linear interpolation from a value to another in a certain time
        """
        start = current_milli_time()
        last = start
        step = float( (self.destination - self.origin) / ( float(self.duration / self.grain) ))
        while (current_milli_time() < (start + self.duration)):
            while (current_milli_time() < last + self.grain):
                pass # wait
            last = current_milli_time()
            self.origin += step
            yield self.origin


class Random(threading.Thread):
    """
    Instanciate a thread for Playing a ramp

    step every 10 ms

    Allow to do several ramps in a same project / scenario / event

    :param target:
    """
    def __init__(self, parent, origin=0, destination=1, duration=1000, grain=10):
        super(Random, self).__init__()
        self.parent = parent
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.grain = grain
        self.start()

    def run(self):
        for step in self.random():
            self.parent.value = step
        self.parent.value = self.destination

    def random(self):
        """
        Generate pseudo-random values in a certain range during a certain time
        """
        start = current_milli_time()
        last = start
        while (current_milli_time() < (start + self.duration)):
            while (current_milli_time() < last + self.grain):
                pass # wait
            last = current_milli_time()
            origin = uniform(self.parent.domain[0], self.parent.domain[1])
            yield origin
