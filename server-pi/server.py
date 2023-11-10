import asyncio
import websockets
import time
from gpiozero import CamJamKitRobot, DistanceSensor

# Define GPIO pins to use for the distance sensor
pin_trigger = 17
pin_echo = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trigger)


# Variables
min_distance = 30.0
left_speed = 0.5
right_speed = 0.5

forward = (left_speed, right_speed)
backward = (-left_speed, -right_speed)
left_turn = (left_speed, -right_speed)
right_turn = (-left_speed, right_speed)

def isInRange():
    dist = sensor.distance * 100
    print("distance: " + str(dist))
    return dist < min_distance



async def handle_connection(websocket, path):
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # forward, backward, left, right, stop 
            match message:
                case "forward":
                    if not isInRange():
                        robot.value = forward
                    else:
                        robot.stop()
                case "backward":
                    robot.value = backward
                case "right":
                    robot.value = left_turn
                case "left":
                    robot.value = right_turn
                case "stop":
                    robot.stop()


    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")




if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)
    
    # Run the server indefinitely
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
