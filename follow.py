
import time  
import keyboard
from gpiozero import CamJamKitRobot, DistanceSensor 

# Define GPIO pins to use for the distance sensor
pin_trigger = 17
pin_echo = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trigger)

# Variables
min_distance = 12
left_speed = 0.3
right_speed = 0.3

forward = (left_speed, right_speed)
backward = (-left_speed, -right_speed)
left = (left_speed, 0)
right = (0, right_speed)


def isInRange(): return (sensor.distance * 100) < min_distance

try:
    while True:
        time.sleep(0.1)
        if isInRange():
            robot.stop()
        elif keyboard.is_pressed("up"):
            robot.value = forward
        elif keyboard.is_pressed("down"):
            robot.value = backward
        elif keyboard.is_pressed("left"):
            robot.value = left
        elif keyboard.is_pressed("right"):
            robot.value = right
        else:
            robot.stop()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()