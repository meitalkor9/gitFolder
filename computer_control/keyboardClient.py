import socket
import keyboard
import threading

stop = False
serverIp = "192.168.1.175"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
sock.connect((serverIp, port))

def receive_keys():
    global stop
    while not stop:
        try:
            data = sock.recv(1)
            if not data:
                continue
            char = data.decode()
            if char == "\n":
                    keyboard.press_and_release("enter")
            elif char == "\t":
                    keyboard.press_and_release("tab")
            elif char == " ":
                    keyboard.press_and_release("space")
            elif char == "\b":
                    keyboard.press_and_release("backspace")
            else:
                    keyboard.write(char)
        except socket.timeout:
            continue
        except (ConnectionResetError, OSError):
            print("Server disconnected.")
            stop =True
            break

thread = threading.Thread(target=receive_keys, daemon=True)
thread.start()

keyboard.wait("esc")
stop = True
sock.close()
print("Stopped by user")
