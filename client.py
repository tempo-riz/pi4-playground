
import socket
import keyboard

# Server configuration
server_address = ('192.168.1.195', 12345)  # Replace with the IP or hostname of your server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)

    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == keyboard.KEY_DOWN:
            command = key_event.name
            if command.lower() == 'q':
                break
            client_socket.sendall(command.encode())
