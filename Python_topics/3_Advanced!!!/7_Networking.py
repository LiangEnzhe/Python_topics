# ----------------------------------------------------------------------
# Networking in Python
# ----------------------------------------------------------------------
# Python's `socket` module provides low-level network communication capabilities.
# For asynchronous and scalable network applications, Python's `asyncio` module
# simplifies the creation of concurrent servers and clients.

# ----------------------------------------------------------------------
# 1. Socket Programming
# ----------------------------------------------------------------------
# A **socket** is an endpoint for sending or receiving data across a network.
# The `socket` module enables creating and using sockets for communication.

import socket

# Example: TCP Server using sockets
def run_tcp_server():
    """TCP Server that listens for incoming connections and responds."""
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 65432))  # Bind to localhost and port 65432
    server_socket.listen(5)  # Listen for up to 5 connections
    print("Server is listening on 127.0.0.1:65432...")

    while True:
        client_socket, client_address = server_socket.accept()  # Accept a connection
        print(f"Connection from {client_address}")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode("utf-8")  # Buffer size is 1024 bytes
        print(f"Received: {data}")
        
        # Send a response back to the client
        client_socket.sendall("Hello, Client!".encode("utf-8"))
        
        # Close the connection
        client_socket.close()

# Example: TCP Client using sockets
def run_tcp_client():
    """TCP Client that connects to a server and sends a message."""
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))  # Connect to the server
    
    # Send a message to the server
    client_socket.sendall("Hello, Server!".encode("utf-8"))
    
    # Receive a response from the server
    response = client_socket.recv(1024).decode("utf-8")
    print(f"Received from server: {response}")
    
    # Close the connection
    client_socket.close()

# Run these functions in separate scripts or threads to test communication.

# ----------------------------------------------------------------------
# 2. Asynchronous Networking with `asyncio`
# ----------------------------------------------------------------------
# Python's `asyncio` module enables asynchronous communication for
# scalable and non-blocking networking applications.

import asyncio

# Example: Asynchronous TCP Server
async def handle_client(reader, writer):
    """Handles a single client connection."""
    client_address = writer.get_extra_info("peername")
    print(f"Connection from {client_address}")

    # Read data from the client
    data = await reader.read(100)  # Read up to 100 bytes
    message = data.decode("utf-8")
    print(f"Received: {message} from {client_address}")
    
    # Send a response to the client
    response = "Hello, Async Client!"
    writer.write(response.encode("utf-8"))
    await writer.drain()  # Ensure all data is sent
    
    print(f"Closing connection to {client_address}")
    writer.close()
    await writer.wait_closed()

async def run_async_tcp_server():
    """Runs an asynchronous TCP server."""
    server = await asyncio.start_server(handle_client, "127.0.0.1", 65432)
    print("Async server running on 127.0.0.1:65432...")
    async with server:
        await server.serve_forever()

# Example: Asynchronous TCP Client
async def run_async_tcp_client():
    """Runs an asynchronous TCP client."""
    reader, writer = await asyncio.open_connection("127.0.0.1", 65432)
    
    # Send a message to the server
    message = "Hello, Async Server!"
    print(f"Sending: {message}")
    writer.write(message.encode("utf-8"))
    await writer.drain()
    
    # Read a response from the server
    data = await reader.read(100)
    print(f"Received from server: {data.decode('utf-8')}")
    
    # Close the connection
    print("Closing connection.")
    writer.close()
    await writer.wait_closed()

# To run the asynchronous server and client:
# asyncio.run(run_async_tcp_server())  # Run this in one script
# asyncio.run(run_async_tcp_client())  # Run this in another script

# ----------------------------------------------------------------------
# Key Differences Between `socket` and `asyncio` Networking
# ----------------------------------------------------------------------
# 1. **Socket Programming**:
#    - Provides low-level control over network communication.
#    - Suitable for simple and blocking I/O tasks.
#    - Manages concurrency with threads or processes.

# 2. **Asyncio Networking**:
#    - Simplifies handling of multiple connections with a single thread.
#    - Uses `async` and `await` for non-blocking communication.
#    - Ideal for scalable applications like chat servers or web sockets.

# ----------------------------------------------------------------------
# 3. Best Practices for Networking Applications
# ----------------------------------------------------------------------

# 1. **Use context managers** for sockets:
#    - Always close sockets properly to free resources.
#    - Example:
#        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#            # Socket operations
#            sock.close()

# 2. **Handle errors gracefully**:
#    - Wrap network calls in `try`/`except` blocks to handle connection issues or timeouts.

# 3. **Optimize performance for scalability**:
#    - Use `asyncio` for handling thousands of concurrent connections efficiently.
#    - Use multiprocessing for CPU-bound tasks combined with networking.

# 4. **Secure connections**:
#    - Use SSL/TLS for encrypted communication in critical applications (e.g., HTTPS).

# 5. **Test and monitor your application**:
#    - Use tools like Wireshark to inspect network traffic.
#    - Monitor server performance with logs and benchmarks.

# ----------------------------------------------------------------------
# Final Thoughts
# ----------------------------------------------------------------------
# Networking in Python provides tools for building robust communication systems:
# - Use `socket` for low-level control.
# - Use `asyncio` for modern, scalable, and asynchronous applications.

# Choose the right approach based on your application's requirements.
