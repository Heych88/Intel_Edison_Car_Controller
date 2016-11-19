#!/usr/bin/python
'''
--------------------------------------------------------------------------------
Module Name:    watchdog.py
Author:         Jon Peterson (PIJ)
Description:    This module implements a simple watchdog timer for Python.
--------------------------------------------------------------------------------
                      Copyright (c) 2012, Jon Peterson
--------------------------------------------------------------------------------
'''

# Imports
from time import sleep
from threading import Timer
import thread

# Watchdog Class
class Watchdog(object):
    
    def __init__(self, timeout=1., userHandler=None):
        ''' Class constructor. The "time" argument has the units of seconds. '''
        self.timeout = timeout
        self.handler = userHandler if userHandler is not None else self.watchdogHandler
        self.triggered = False
        
        return
        
    def start(self):
        ''' Starts the watchdog timer. '''
        self.timer = Timer(self.timeout, self.watchdogHandler)
        self.timer.daemon = True
        self.timer.start()
        return
        
    def reset(self):
        ''' Reset watchdog timer. '''
        self.stop()
        self.start()
        return
        
        #def reset(self):
        #self.timer.cancel()
        #self.timer = Timer(self.timeout, self.handler)
        
    def watchdogHandler(self):
        '''
        This internal method gets called when the timer triggers. A keyboard 
        interrupt is generated on the main thread. The watchdog timer is stopped 
        when a previous event is tripped.
        '''
        print 'Watchdog event...'
        self.stop()
        #thread.interrupt_main()
        self.triggered = True
        return

    def stop(self):
        ''' Stops the watchdog timer. '''
        self.timer.cancel()
