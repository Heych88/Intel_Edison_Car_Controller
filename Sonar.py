# -*- coding: utf-8 -*-
"""
**********************************************************************
Created on Sun Nov 20 10:31:05 2016

* Filename    : Sonar.py
* Description : Takes a distance reading from an ultrasonic sensor rotating on 
*               a servo and returns a 2D layout of objects for the given servo 
*               angles.
*
* Original    : This class has been built ontop of the SunFounder servo.py
*               The original autor and details are below
* Author      : Haidyn
* Update      : 
**********************************************************************
"""

import Ultrasonic
import Servo
import time

class Sonar:
    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Sonar.py":'
    
    servoStart = 12
    servoStop = 182
    
    def __init__(self, sonicTrig, sonicEcho, servoChannel):
        self.trigger = sonicTrig
        self.echo = sonicEcho
        self.servoChannel = servoChannel
        
        if self._DEBUG:
            print self._DEBUG_INFO, "Debug on"
            
        self.servo = Servo.Servo(servoChannel,self.servoStart,
                                 self.servoStart - 1,
                                 self.servoStop)
        self.ultra = Ultrasonic.Ultrasonic(sonicTrig, sonicEcho)
        
        
    def run(self):
        self.servo.reset()
        time.sleep(0.1)
        
        for angle in range(self.servoStart, self.servoStop+1, 1):
            self.servo.turn(angle)            
            time.sleep(0.035) 
            distance = self.ultra.get_distance()
            print (distance)            
    
    def set_debug(self, debug):
        ''' Set if debug information shows '''
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

            if self._DEBUG:
                print self._DEBUG_INFO, "Set debug on"
            else:
                print self._DEBUG_INFO, "Set debug off"