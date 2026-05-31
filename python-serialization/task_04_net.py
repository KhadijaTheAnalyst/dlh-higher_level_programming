#!/usr/bin/env python3
"""
Client-Server Application with Serialization

This module demonstrates serialization and network communication.
The server receives a dictionary from the client, deserializes it,
and processes it.
"""

import socket
import json


def start_server(host='127.0.0.1', port=5000):
    """
    Start a server that listens for incoming connections.
    
    Receives a serialized dictionary from the client, deserializes it,
    and prints the received data.
    
    Args:
        host (str): The host address to bind to (default: localhost)
        port (int): The port number to listen on (default: 5000)
    """
    try:
        # Step 1: Create socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Step 2: Bind to host and port
        server_socket.bind((host, port))

        # Step 3: Listen for connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        # Step 4: Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established from {client_address}")

        # Step 5: Receive data
        data = client_socket.recv(1024).decode('utf-8')

        # Step 6: Deserialize JSON to dictionary
        received_dict = json.loads(data)

        # Step 7: Print the received dictionary
        print("Received Dictionary from Client:")
        print(received_dict)

        # Step 8: Close connections
        client_socket.close()
        server_socket.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def send_data(data_dict, host='127.0.0.1', port=5000):
    """
    Send a Python dictionary to the server after serializing it.
    
    Args:
        data_dict (dict): The dictionary to send
        host (str): The server host address (default: localhost)
        port (int): The server port number (default: 5000)
    """
    try:
        # Step 1: Create socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Step 2: Connect to server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Step 3: Serialize dictionary to JSON
        serialized_data = json.dumps(data_dict)

        # Step 4: Send the serialized data
        client_socket.sendall(serialized_data.encode('utf-8'))
        print(f"Sent data to server: {data_dict}")

        # Step 5: Close connection
        client_socket.close()

    except socket.error as e:
        print(f"Connection error: {e}")
    except json.JSONEncodeError as e:
        print(f"JSON encoding error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    pass
