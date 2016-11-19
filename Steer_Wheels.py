#!/usr/bin/env python
'''
**********************************************************************
* Filename    : front_wheels
* Description : A module to control the front wheels of RPi Car
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''
from Servo import *
#import filedb

class Steer_Wheels(object):
    ''' Front wheels control class '''
    STEER_SERVO_ID = 0
    MAX_STEER_ANGLE = 35
    STRAIGHT_ANGLE = 122

    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "front_wheels.py":'

    def __init__(self, config_file=None):
        ''' setup channels and basic stuff '''
        if self._DEBUG:
            print self._DEBUG_INFO, "Debug on"
            #self.db = filedb.fileDB()
            #self.turning_offset = self.db.get('turning_offset', default_value=0)

        self.wheel = Servo(self.STEER_SERVO_ID)
        self.wheel.set_base_position(self.STRAIGHT_ANGLE)
        self.wheel.set_min_limit(self.MAX_STEER_ANGLE)
        self.wheel.set_max_limit(self.MAX_STEER_ANGLE)      
        
        if self._DEBUG:
            print self._DEBUG_INFO, 'Front wheel PEM channel:', self.STEER_SERVO_ID
            print self._DEBUG_INFO, 'Front wheel base value:', self.STRAIGHT_ANGLE

        self.angle = {"left":self.MAX_STEER_ANGLE, "straight":self.STRAIGHT_ANGLE, "right":self.MAX_STEER_ANGLE}
        if self._DEBUG:
            print self._DEBUG_INFO, 'left angle: %s, straight angle: %s, right angle: %s' % (self.angle["left"], self.angle["straight"], self.angle["right"])

    def turn_left(self, angle):
        ''' Turn the front wheels left '''
        if self._DEBUG:
            print self._DEBUG_INFO, "Turn left"
        self.wheel.turn(angle*-1) #self.angle["left"])

    def turn_straight(self):
        ''' Turn the front wheels back straight '''
        if self._DEBUG:
            print self._DEBUG_INFO, "Turn straight"
        self.wheel.reset() # turn(self.angle["straight"])

    def turn_right(self, angle):
        ''' Turn the front wheels right '''
        if self._DEBUG:
            print self._DEBUG_INFO, "Turn right"
        self.wheel.turn(angle) #self.angle["right"])

    def set_debug(self, debug):
        ''' Set if debug information shows '''
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

        if self._DEBUG:
            print self._DEBUG_INFO, "Set debug on"
            print self._DEBUG_INFO, "Set wheel debug on"
            self.wheel.set_debug(True)
        else:
            print self._DEBUG_INFO, "Set debug off"
            print self._DEBUG_INFO, "Set wheel debug off"
            self.wheel.set_debug(False)

    