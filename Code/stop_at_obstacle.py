# CamJam EduKit 3 - Robotics
# Worksheet 9 - Obstacle Avoidance

import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import GPIO Zero Libraries

# Define GPIO pins to use for the distance sensor
pintrigger = 17
pinecho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# Distance Variables
min_distance = 15.0

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("distance: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False



try:
    while True:
        time.sleep(0.1)
        if isnearobstacle(min_distance):
            robot.stop()
        else:
            robot.value = motorforward
            
            

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
