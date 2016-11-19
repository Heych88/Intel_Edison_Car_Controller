# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:42:03 2016

@author: haidyn.mcleod
"""
import mraa
import time
import math
    
def isr_trigger(obj):
    """ Encoder interupt function """
    obj.isr_encoder_count(obj.trigger.read()) # call function within the class obj


class Encoder (object):
    
    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Encoder.py":'
    
    def __init__(self, channel, teath=10, diameter=65.):
        self.pin = channel
        self.teath = teath-1  # number of detectable edges pre revolution, starting at 0 
        self.count = 0
        self.revolution = 0
        self.wheelCircum = math.pi*diameter
        
        self.trigger = mraa.Gpio(channel)
        self.trigger.dir(mraa.DIR_IN)
        self.trigger.isr(mraa.EDGE_RISING , isr_trigger, self)
        
       # self.edge = self.trigger.read()
        
        if self._DEBUG:
            print (self._DEBUG_INFO, '__init__(), Initalise on channel {0}, with {1} encoder teath'.format(channel, teath))
        

    def isr_encoder_count(self, edge):
        self.edge = edge
        if self.revolution == 0:
            self.startTime = time.time()
            
        if self.count >= self.teath:
            self.count = 0
            self.revolution +=1
        else:
            self.count+=1
            
        if (((self.revolution % 3) == 0) and (self.count == 0)):
            self.timeDiff = time.time() - self.startTime 
            self.startTime = time.time()
            
            self.encoder_speed(self.timeDiff)
            
            if self._DEBUG:
                print (self._DEBUG_INFO, 'isr_encoder_count(), time between revolution, ',self.timeDiff,'s')
        
        if self._DEBUG:
            print (self._DEBUG_INFO, 'isr_encoder_count(), Encoder count = ', self.count)
        
    def encoder_finish(self):
        self.trigger.isrExit()
        
        if self._DEBUG:
            print (self._DEBUG_INFO, 'encoder_finish()')
        
    def encoder_speed(self, time):
        self.speed = (self.wheelCircum*3.)/time
        
        if self._DEBUG:
            print (self._DEBUG_INFO, 'encoder_speed(), time difference = ', time, 's, speed = ', self.speed, ' mm/s')
        
    def set_debug(self, debug):
        ''' Set if debug information shows '''
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

        if self._DEBUG:
            print self._DEBUG_INFO, 'Set debug on'
        else:
            print self._DEBUG_INFO, 'Set debug off'