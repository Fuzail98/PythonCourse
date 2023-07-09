import socket

'''
mySocket = socket.socket()
mySocket.bind()  # Server
mySocket.listen()  # Server, pass number of connections
mySocket.accept()
mySocket.connect()  # Client

# After connection between server and client
mySocket.send()  # Pass string.encode()
mySocket.recv()  # Input is number of bytes to be received.
# After recieving, do string.decode()

mySocket.close()
'''


hacker_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM means TCP
# SOCK_DGRAM means UDP

# Now we will bind this server to attacker IP addresses
ip_to_listen = "0.0.0.0"
port = 8788

my_socket_address = (ip_to_listen, port)
hacker_server_socket.bind(my_socket_address)

hacker_server_socket.listen(5)

client_socket, client_address = hacker_server_socket.accept()

print(client_address)
print(client_socket.recv(1024).decode())

client_socket.close()
hacker_server_socket.close()
