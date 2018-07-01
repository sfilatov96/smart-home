# -*- coding: utf-8 -*-
from sensors.motion import MotionSensor


def detect_motion__in_flat():
    def func():
        print "detect!"

    sensor = MotionSensor()
    sensor.read(callback=func)