#!/usr/bin/env python
'''
**********************************************************************
* Filename    : TB6612.py
* Description : A driver module for TB6612
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''
#import RPi.GPIO as GPIO
import mraa
import PCA9685

class Motor(object):
    ''' Motor driver class
    Set channel_1 to the GPIO channel which connect to In1, In4, 
    Set motor_B to the GPIO channel which connect to GND,
    Both GPIO channel use BCM numbering;
    Set pwm_channel to the PWM channel which connect to PCA9685 8, 9,
    PWM channel using PCA9685, Set pwm_address to your address, if is not 0x40
    Set debug to True to print out debug informations.
    '''
    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Motor.py":'

    def __init__(self, channel_1, channel_2, pwm_channel, pwm_address=0x40, move_forward=1):
        '''Init a motor on giving dir. channel and PWM channel.'''
        if self._DEBUG:
            print self._DEBUG_INFO, "Debug on"
        self.channel_1 = channel_1
        self.channel_2 = channel_2
        self.pwm_channel = pwm_channel
        self.move_forward = move_forward
        self.forward = self.move_forward

        self.backward = 0

        self.pwm = PCA9685.PWM(address=pwm_address)
        self.set_debug(self._DEBUG)
        #GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BCM)

        if self._DEBUG:
            print self._DEBUG_INFO, 'setup motor direction channel at', channel_1
            print self._DEBUG_INFO, 'setup motor pwm channel at', pwm_channel
        #GPIO.setup(self.channel_1, GPIO.OUT)
        self.inA = mraa.Gpio(self.channel_1)    #setup io pin as inA
        self.inA.dir(mraa.DIR_OUT)              # set io pin to out
        self.inB = mraa.Gpio(self.channel_2)
        self.inB.dir(mraa.DIR_OUT)

    def _map(self, x, in_min, in_max, out_min, out_max):
        '''To map the value from arange to another'''
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def set_speed(self, speed):
        ''' Set Speed with giving value '''
        if self._DEBUG:
            print self._DEBUG_INFO, 'Set speed to: ', speed
        self.speed = self._map(speed, 0, 100, 0, 4095)
        if self._DEBUG:
            print self._DEBUG_INFO, 'Speed pwm: ', speed
        self.pwm.set_value(self.pwm_channel, 0, self.speed)

    def go_forward(self):
        ''' Set the motor direction to forward '''
        self.inA.write(self.forward)
        self.inB.write(self.backward)
        if self._DEBUG:
            print self._DEBUG_INFO, 'Motor moving forward (%s)' % str(self.forward)

    def go_backward(self):
        ''' Set the motor direction to backward '''
        self.inA.write(self.backward)
        self.inB.write(self.forward)
        if self._DEBUG:
            print self._DEBUG_INFO, 'Motor moving backward (%s)' % str(self.backward)

    def stop(self):
        ''' Stop the motor by giving a 0 speed '''
        if self._DEBUG:
            print self._DEBUG_INFO, 'Motor stop'
        self.set_speed(0)
        
    def brake(self, speed):
        ''' Slow the motor at a giving speed '''
        if self._DEBUG:
            print self._DEBUG_INFO, 'brake(), Motor breaking at speed %d', speed
        self.inA.write(self.forward)
        self.inB.write(self.forward)
        self.set_speed(speed)        

    def set_move_forward(self, value):
        ''' Set move_forward for much user-friendly '''
        if value not in (True, False):
            raise ValueError('move_forward value must be Bool value, not"{0}"').format(value)
        self.forward = value
        self.backward = not self.forward
        if self._DEBUG:
            print self._DEBUG_INFO, 'Set movement to %d' % self.move_forward

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