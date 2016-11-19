# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 23:18:13 2016

@author: haidyn.mcleod
"""

#!/usr/bin/env python
'''
**********************************************************************
* Filename    : Drive_wheels.py
* Description : A module to control the back wheels of RPi Car
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''

import Motor
import Encoder
#import filedb

class Drive_Wheels(object):
    ''' Back wheels control class '''
    Motor_A1 = 13
    Motor_A2 = 12
    Motor_B1 = 11
    Motor_B2 = 10
    
    encoderLeft = 8
    encoderRight = 7

    PWM_A = 9
    PWM_B = 8

    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "back_wheels.py":'

    def __init__(self):
        ''' Init the direction channel and pwm channel '''
        if self._DEBUG:
            print self._DEBUG_INFO, "Debug on"
        self.forward_A = 1
        self.forward_B = 1

        #self.db = filedb.fileDB()

        #self.forward_A = self.db.get('forward_A', default_value=True)
        #self.forward_B = self.db.get('forward_B', default_value=True)

        self.left_wheel = Motor.Motor(self.Motor_A1, self.Motor_A2, self.PWM_A)
        self.right_wheel = Motor.Motor(self.Motor_B1, self.Motor_B2, self.PWM_B)
        
        # set the logic value for forward movement, invert if motor runs Back
        self.left_wheel.set_move_forward(self.forward_A)
        self.right_wheel.set_move_forward(self.forward_B)

        if self._DEBUG:
            print self._DEBUG_INFO, 'Set left wheel IN1 to IO #%d, IN2 to IO #%d, PWM channel to IO %d' % (self.Motor_A1, self.Motor_A2, self.PWM_A)
            print self._DEBUG_INFO, 'Set right wheel IN1 to IO #%d, IN2 to IO #%d, PWM channel to IO %d' % (self.Motor_B1, self.Motor_B2, self.PWM_B)

    def forward(self):
        ''' Move both wheels forward '''
        self.left_wheel.go_forward()
        self.right_wheel.go_forward()
        if self._DEBUG:
            print self._DEBUG_INFO, 'Running forward'

    def backward(self):
        ''' Move both wheels backward '''
        self.left_wheel.go_backward()
        self.right_wheel.go_backward()
        if self._DEBUG:
            print self._DEBUG_INFO, 'Running backward'

    def stop(self):
        ''' Stop both wheels '''
        self.left_wheel.stop()
        self.right_wheel.stop()
        if self._DEBUG:
            print self._DEBUG_INFO, 'Stop'

    def set_speed(self, speed):
        ''' Set moving speeds '''
        self.left_wheel.set_speed(speed)
        self.right_wheel.set_speed(speed)
        if self._DEBUG:
            print self._DEBUG_INFO, 'Set speed to', speed

    def set_debug(self, debug):
        ''' Set if debug information shows '''
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

        if self._DEBUG:
            print self._DEBUG_INFO, "Set debug on"
            print self._DEBUG_INFO, "Set left wheel and right wheel debug on"
            self.left_wheel.set_debug(True)
            self.right_wheel.set_debug(True)
        else:
            print self._DEBUG_INFO, "Set debug off"
            print self._DEBUG_INFO, "Set left wheel and right wheel debug off"
            self.left_wheel.set_debug(False)
            self.right_wheel.set_debug(False)