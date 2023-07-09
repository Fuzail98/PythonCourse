import socket

port = 8788

targetClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
targetClient.connect(("192.168.200.8", port))
targetClient.send('Hello'.encode())
