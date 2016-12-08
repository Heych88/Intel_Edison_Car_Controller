# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 16:08:42 2016

@author: haidyn.mcleod
"""

#import KeyLogger_tk2
import Servo
import Steer_Wheels
import Drive_Wheels
import Encoder
import time
import Ultrasonic
import Sonar
#import curses

"""def keyinput ():
    screen = curses.initscr()
    #try:
    curses.noecho()
    #curses.curs_set(0)
    screen.keypad(1)
    #screen.addstr("Press a key")
    event = screen.getch()
    
    #if event == curses.KEY_UP:
        
    #finally:
    #    curses.endwin()
    return event"""
    


def test():
    '''Servo driver test on channel 1'''
    
    try:
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """STEER_SERVO_ID = 0
        _STEER_ANGLE = 40
        
        a = Servo.Servo(STEER_SERVO_ID)
        a.set_debug(True)
        a.set_base_position(122) # set the sterring center position
        a.set_max_limit(_STEER_ANGLE)   # set the max angle past base position for the steering
        a.set_min_limit(-1*_STEER_ANGLE) # set the min angle past base position for the steering
    
        a.reset()
        time.sleep(3)
        a.turn(120)
        time.sleep(3)
        a.turn(-1*_STEER_ANGLE)
        time.sleep(3)
        a.reset()"""
    
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
        """front_wheels = Steer_Wheels.Steer_Wheels()
        front_wheels.set_debug(True)
    
        while True:
            print "turn_left"
            front_wheels.turn_left(40.)
            time.sleep(5)
            print "turn_straight"
            front_wheels.turn_straight()
            time.sleep(5)
            print "turn_right"
            front_wheels.turn_right(30.)
            time.sleep(5)
            print "turn_straight"
            front_wheels.turn_straight()
            time.sleep(5)"""
        
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        TRIGGER = 6
        ECHO    = 5
        CHANNEL = 1
    
        #ultra = Ultrasonic.Ultrasonic(GPIO_TRIGGER, GPIO_ECHO)
        sonar = Sonar.Sonar(TRIGGER, ECHO, CHANNEL)
        
        while True:
            sonar.run()
        
        """while True:
            distance = ultra.get_distance()
            
            print ('Distance = %.1f' % distance)"""
            

        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """while active:
            direction = keyinput() 
            
            #if direction in [int('Q'), int('q')]:
                #    active = False
        
                if direction == curses.KEY_LEFT:
                    steerVal += 1
                    #print("Left Arrow Key pressed")
                elif direction == curses.KEY_RIGHT:
                    steerVal -= 1
                    #print("Right Arrow Key pressed")
            
            ""if steerVal <= (a.get_offset - _STEER_MAX/2):
                steerVal = a.get_offset - _STEER_MAX/2
            elif steerVal >= (a.get_offset + _STEER_MAX/2):
                steerVal = a.get_offset + _STEER_MAX/2""
          
            print steerVal
            a.turn(steerVal)
            
            time.sleep(0.05)"""
        
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #back_wheels = Drive_Wheels.Drive_Wheels()
        #DELAY = 0.1
        #back_wheels.forward()
        """for i in range(0, 100):
            back_wheels.set_speed(i)
            print "Speed =", i
            time.sleep(DELAY)
        for i in range(100, 0, -1):
            back_wheels.set_speed(i)
            print "Speed =", i
            time.sleep(DELAY)
            
        back_wheels.backward()
        for i in range(0, 100):
            back_wheels.set_speed(i)
            print "Speed =", i
            time.sleep(DELAY)
        for i in range(100, 0, -1):
            back_wheels.set_speed(i)
            print "Speed =", i
            time.sleep(DELAY)"""
        
        #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """right_wheel = Encoder.Encoder(7)
        right_wheel.set_debug(True)
        
        while right_wheel.revolution < 31:
            back_wheels.set_speed(15)
            time.sleep(0.02)
        
        back_wheels.stop"""
        
        
    except KeyboardInterrupt:
        #back_wheels.stop()
        #right_wheel.encoder_finish()
        print "Stopping everything"
    
    finally:
        print "Stopping everything"
        #right_wheel.encoder_finish()
        #back_wheels.stop()

def install():
    all_servo = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
    for i in range(16):
        all_servo[i] = Servo(i)
    for servo in all_servo:
        servo.turn(90)

if __name__ == '__main__':
    import sys
   
    if len(sys.argv) == 2:
        if sys.argv[1] == "install":
            install()
    else:
        test()