import socket
from gpiozero import CamJamKitRobot, DistanceSensor

# Define GPIO pins to use for the distance sensor
pin_trigger = 17
pin_echo = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trigger)

# Variables
min_distance = 15.0
left_speed = 0.3
right_speed = 0.3

forward = (left_speed, right_speed)
backward = (-left_speed, -right_speed)
left_turn = (left_speed, 0)
right_turn = (0, right_speed)

def isInRange():
    if (sensor.distance * 100) < min_distance:
        return True
    else:
        return False

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

                if command == "W":
                    robot.value = forward
                elif command == "S":
                    robot.value = backward
                elif command == "A":
                    robot.value = left_turn
                elif command == "D":
                    robot.value = right_turn

                print(f"Received command: {command}")
