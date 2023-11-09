import socket

# Server configuration
server_address = ('192.168.1.195', 12345)  # Replace with the IP or hostname of your server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)

    while True:
        command = input("Enter a command (W, A, S, D) or 'q' to quit: ")
        if command.lower() == 'q':
            break
        client_socket.sendall(command.encode())
