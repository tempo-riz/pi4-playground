import socket
import time
from gpiozero import CamJamKitRobot, DistanceSensor

# Define GPIO pins to use for the distance sensor
pin_trigger = 17
pin_echo = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trigger)

# Variables
min_distance = 30.0
left_speed = 0.3
right_speed = 0.3

forward = (left_speed, right_speed)
backward = (-left_speed, -right_speed)
left_turn = (left_speed, -right_speed)
right_turn = (-left_speed, right_speed)

def isInRange():
    dist = sensor.distance * 100
    print("distance: " + str(dist))
    return dist < min_distance

# Server configuration
host = ''  # Listen on all available interfaces
port = 12345  # Choose a port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening on port {port}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                command = data.decode().strip()

                if command == "haut":
                    print("up")
                    if(isInRange()):
                        robot.stop()
                    else:
                        robot.value = forward
                elif command == "bas":
                    print("down")
                    robot.value = backward
                elif command == "droite":
                    print("right")
                    robot.value = left_turn
                elif command == "gauche":
                    print("left")
                    robot.value = right_turn
                else: # any other command will stop
                    robot.stop()
                
                time.sleep(0.1)

