#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Author : Matt Hawkins
# Date   : 09/01/2013

# Import required Python libraries
import time
import mraa
import Watchdog

class Ultrasonic:
    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Ultrasonic.py":'
    
    def __init__(self, triggerChannel, echoChannel):
        # Define GPIO to use on Pi
        self.GPIO_TRIGGER = triggerChannel
        self.GPIO_ECHO = echoChannel
        #self.GPIO_SERVO = servoChannel
        
        self.watchdog = Watchdog.Watchdog(0.01)

        # Set pins as output and input
        self.trigger = mraa.Gpio(self.GPIO_TRIGGER)  # Trigger
        self.trigger.dir(mraa.DIR_OUT)
        self.echo = mraa.Gpio(self.GPIO_ECHO)      # Echo
        self.echo.dir(mraa.DIR_IN)
        
        if self._DEBUG:
            print self._DEBUG_INFO, '__init__(), setup trigger = {0}, echo = {1}, servo = {2}'.format(self.GPIO_TRIGGER,self.GPIO_ECHO,self.GPIO_SERVO)
    
    def get_distance(self):    
        #self.watchdog.start()

        try:
            self.trigger.write(0)    # Set trigger to False (Low)
            time.sleep(0.005)    # Allow module to settle
            self.watchdog.start()

            self.trigger.write(1)    # Send 10us pulse to trigger
            time.sleep(0.00001)
            self.trigger.write(0)
            start = time.time()

            while ((self.echo.read() == 0)and(self.watchdog.triggered == False)):
                start = time.time()

            while ((self.echo.read()==1)and(self.watchdog.triggered == False)):
                stop = time.time()
            
            self.watchdog.stop()
        
        except Watchdog:
            print ('watchdog timed out')
            
        if self.watchdog.triggered == True:
            self.watchdog.triggered = False
            #self.watchdog.start()
            distance = -1.
        else:
            #self.watchdog.stop()      
            elapsed = stop-start    # Calculate pulse length
            # Distance pulse travelled in that time is time
            # multiplied by the speed of sound (cm/s)
            distance = elapsed * 34300.
            # That was the distance there and back so halve the value
            distance = distance / 2.
        
        if self._DEBUG:
            print self._DEBUG_INFO, 'get_distance(), distance = %.1f' % distance

        return distance
        

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