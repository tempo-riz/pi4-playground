import asyncio
import websockets

async def handle_connection(websocket, path):
    try:
        async for message in websocket:
            # Here, you can handle the received message (direction)
            print(f"Received direction: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_connection, "0.0.0.0", 8765)
    
    # Run the server indefinitely
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
