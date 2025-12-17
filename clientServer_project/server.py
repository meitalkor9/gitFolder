import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8080))
sock.listen(5) 
print("Server listening...")

while True:
    connection, address = sock.accept()
    print("Connected from", address)
    command = connection.recv(1024).decode()

    if command == "uploadFile":
        filename = connection.recv(1024).decode()
        filename = os.path.basename(filename)
        with open(filename, "wb") as f:
            while True:
                chunk = connection.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
        print("File received:", filename)

    elif command == "downloadFile":
        filename = connection.recv(1024).decode()
        filename = os.path.basename(filename)
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    connection.send(chunk)
            print("File sent:", filename)
        else:
            print("File not found:", filename)
    else:
        print("Unknown command:", command)
    connection.close() 
