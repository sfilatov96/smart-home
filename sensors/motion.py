# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


class MotionSensor(object):
    def __init__(self, delay=1, pin=16):
        """
        
        :param delay: float
        :param pin: int
        """
        self.pin = pin
        self.delay = delay
        
    def read(self, callback):
        while True:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin, GPIO.IN)
            GPIO.wait_for_edge(self.pin, GPIO.RISING)
            signal = GPIO.input(self.pin)
            callback()
            
            time.sleep(self.delay)
