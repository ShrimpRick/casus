from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import hub
import runtime
import sys
import system
import mindstorms
from mpy_robot_tools.rc import RCReceiver, R_STICK_VER, L_STICK_HOR, SETTING1, L_TRIGGER

import bluetooth
import random
import struct
import time
import micropython
import ubinascii


from micropython import const


# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()

hub = MSHub()



color_sensor = ColorSensor('A')# collor
motor_c = Motor('C')# Wielen
motor_e = Motor('E')# Wielen
distance_sensor = DistanceSensor('D')# Afstandssensor



motor_pair = MotorPair('C', 'E')# bofe wielen
motor_pair.set_default_speed(-100)
# motor_pair.start()


hub.speaker.play_sound("yes")
# while True:
#         motor_c.start()
#         motor_e.start()
