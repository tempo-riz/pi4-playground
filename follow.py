
import time  
from gpiozero import CamJamKitRobot, DistanceSensor 

# Define GPIO pins to use for the distance sensor
pin_trigger = 17
pin_echo = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trigger)

# Variables
min_distance = 15.0
left_speed = 0.1
right_speed = 0.1

forward = (left_speed, right_speed)
backward = (-left_speed, -right_speed)
left = (left_speed, 0)
right = (0, right_speed)


def isInRange():
    if (sensor.distance * 100) < min_distance:
        return True
    else:
        return False

try:
    while True:
        time.sleep(0.1)
        if isInRange():
            robot.value = backward
        else:
            robot.value = forward

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
