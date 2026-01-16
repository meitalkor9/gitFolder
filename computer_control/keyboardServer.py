import socket
import keyboard
import threading
import time
serverIp = "192.168.1.175"
port = 8080
stop = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverIp, port))
sock.listen(1)
print("Waiting for client to connect...")
connection, address = sock.accept()
connection.settimeout(1)
print("Connected with", address)

def send_key(event):
    global stop
    if stop:
        return
    try:
        if event.name == "esc":
            stop = True
            print("ESC pressed, closing connection...")
            connection.close()
            sock.close()
            return
        elif event.name == "space":
            connection.send(b" ")
        elif event.name == "enter":
            connection.send(b"\n")
        elif event.name == "tab":
            connection.send(b"\t")
        elif event.name == "backspace":
            connection.send(b"\b")
        elif len(event.name) == 1:
            connection.send(event.name.encode())
    except (BrokenPipeError, ConnectionResetError):
        stop = True
        print("Client disconnected, closing server...")
        try:
            connection.close()
            sock.close()
        except:
            pass

keyboard.on_release(send_key)
while not stop:
     time.sleep(0.1)
print("Server stopped")
