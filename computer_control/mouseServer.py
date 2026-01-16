import socket
from pynput.mouse import Button, Controller, Listener
import threading
import time
import keyboard

serverIp ="0.0.0.0"
port=8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((serverIp, port))
sock.listen(1)
print("Waiting for client to connect...")
connection, address = sock.accept()

#if address[0] != clientIp:
    #connection.close()
    #raise SystemExit(f"This is not the correct client: {address[0]}")

def stopServer():
    global stop
    keyboard.wait("esc") 
    print("ESC pressed, closing connection...")
    connection.sendall(b"stop\n")
    stop=True
    connection.close()
    sock.close()
    print("Server closed")

print("Connected with", address)
mouse=Controller()
stop=False

def move_mouse():
    global stop
    prev_pos = None
    while not stop:
        x,y = mouse.position
        if prev_pos != (x, y):
            prev_pos = (x, y)
            data = f"{x},{y}\n".encode()
            try:
                connection.sendall(data)
            except:
                connection.close()
                stop = True
        time.sleep(0.1)


def click_mouse(x, y, button, pressed):
    if not pressed:
        return
    try:
        if button == Button.left:
            connection.sendall(b"left\n")
        elif button == Button.right:
            connection.sendall(b"right\n")
    except:
        pass

def scroll_mouse(x, y, dx, dy):
    try:
        if dy > 0:
            connection.sendall(b"SCROLL_UP\n")
        elif dy < 0:
            connection.sendall(b"SCROLL_DOWN\n")
    except:
        pass

threading.Thread(target=move_mouse, daemon=True).start()
threading.Thread(target=stopServer, daemon=True).start()
try:
    with Listener(on_click=click_mouse, on_scroll=scroll_mouse) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Stopped by user")
except Exception as e:
    print("Listener error:", e)
finally:
    stop = True
    connection.close()
    sock.close()
