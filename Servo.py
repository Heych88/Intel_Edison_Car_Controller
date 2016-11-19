#!/usr/bin/env python
'''
**********************************************************************
* Filename    : Servo.py
* Description : Driver module for servos controlled through a PCA9685
*               This class must have a base/start position setup which
*               all movment angles are based off. Positive values move 
*               one way and negitive values move the other.
*               'set_basePosition(angle)' to set start position at angle
*               from 0 to 180 degrees
*               'turn(angle)' to turn servo from base position, i.e 
*               'turn(30)' adds 30 degrees to the base position
*
* Original    : This class has been built ontop of the SunFounder servo.py
*               The original autor and details are below
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''

"""
Servo
"""

import PCA9685

def _map(x, in_min, in_max, out_min, out_max):
    '''To map the value from arange to another'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class Servo(object):
    '''Servo driver class'''
    _MIN_PULSE_WIDTH = 600
    _MAX_PULSE_WIDTH = 2400
    _DEFAULT_PULSE_WIDTH = 1500
    _FREQUENCY = 60

    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Servo.py":'

    def __init__(self, channel, basePosition=0, lock=True, minLimit=0, maxLimit=180):
        ''' Init a servo on specific channel, this basePosition '''
        if channel<0 or channel > 16:
            raise ValueError("Servo channel \"{0}\" is not in (0, 15).".format(channel))
	
        if self._DEBUG:
            print self._DEBUG_INFO, "Debug on"
		
        self.channel = channel
        self.basePosition = basePosition
        self.lock = lock
        self.minLimit = minLimit
        self.maxLimit = maxLimit

        self.pwm = PCA9685.PWM()
        self.pwm.set_frequency(60)
        self.pwm.set_value(self.channel, 0, self._DEFAULT_PULSE_WIDTH)

    def _angle_to_analog(self, angle):
        ''' Calculate 12-bit analog value from giving angle '''
        pulse_wide   = _map(angle, 0, 180, self._MIN_PULSE_WIDTH, self._MAX_PULSE_WIDTH)
        analog_value = int(float(pulse_wide) / 1000000 * self._FREQUENCY * 4096)
        if self._DEBUG:
            print self._DEBUG_INFO, '_angle_to_analog(), Angle %d equals Analog_value %d' % (angle, analog_value)
        return analog_value
		
    def set_base_position(self, angle):
        ''' Set the base/start postion for the servo '''
        if angle > self.maxLimit:
            angle = self.maxLimit
        elif angle < self.minLimit:
            angle = self.minLimit
            
        self.basePosition = angle #self._angle_to_analog(value)
        if self._DEBUG:
            print self._DEBUG_INFO, 'set_basePosition(), basePosition to %d' % self.basePosition
            
    def get_base_position(self):
        ''' get basePosition for much user-friendly '''
        if self._DEBUG:
            print self._DEBUG_INFO, 'get_basePosition(), basePosition = %d' % self.basePosition
        return self.basePosition
        
    def set_max_limit(self, angle):
        """ set the max angle of the servor from the base position """
        angle = self.basePosition + angle
        if angle > 360:
            angle = 360 # set maximum angle of 360
        elif angle < self.basePosition:
            angle = self.basePosition # set minimum angle of basePosition
        
        self.maxLimit = angle
        if self._DEBUG:
            print self._DEBUG_INFO, 'set_max_limit(), maxLimit with base = %d' % self.maxLimit
            
    def get_max_limit(self):
        """ get the current max angle of the servor from the base position """        
        if self._DEBUG:
            print self._DEBUG_INFO, 'get_max_limit(), maxLimit with base = %d' % self.maxLimit
        return self.maxLimit - self.basePosition
        
    def set_min_limit(self, angle):
        """ set the min angle of the servor from the base position """
        angle = self.basePosition - angle
        if angle < 0:
            angle = 0 # set minimum angle of 0
        elif angle > self.basePosition:
            angle = self.basePosition # set minimum angle of basePosition 
            
        self.minLimit = angle
        if self._DEBUG:
            print self._DEBUG_INFO, 'set_min_limit(), minLimit with base = %d' % self.minLimit
            
    def get_min_limit(self):
        """ get the current min angle of the servor from the base position """        
        if self._DEBUG:
            print self._DEBUG_INFO, 'get_max_limit(), minLimit with base = %d' % self.minLimit
        return self.minLimit - self.basePosition

    def turn(self, angle):
        ''' Turn the servo with giving angle. '''
        if self.lock:
            # add the base position to the angle
            angle = self.basePosition + angle
            if angle > self.maxLimit:
                angle = self.maxLimit
            elif angle < self.minLimit:
                angle = self.minLimit
            #check that the angle is within the movment parameters
            if angle<self.minLimit or angle>self.maxLimit:
                raise ValueError("Servo \"{0}\" turn angle \"{1}\" is not in ({2}, {3}).".format(self.channel, angle, self.minLimit, self.maxLimit))
                
            # Get the PWM value for the desired angle from the base position
            val = self._angle_to_analog(angle) 
            self.pwm.set_value(self.channel, 0, val)
            if self._DEBUG:
                print self._DEBUG_INFO, 'turn(), Turn angle + base = %d' % angle
                
    def reset(self):
        """ reset the servo to its base position"""
        self.turn(0) #self.basePosition)
        if self._DEBUG:
            print self._DEBUG_INFO, 'reset(), Turn to centre at angle = %d' % self.basePosition
        

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
