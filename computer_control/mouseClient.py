import socket
from pynput.mouse import Button, Controller
def main():
    serverIp = "192.168.1.175"
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIp, port))
    sock.settimeout(1)
    mouse = Controller()
    buffer = ""
    try:
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    break
            except socket.timeout:
                continue
            buffer += data.decode()
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                
                if line=="stop":
                  print("Received stop")
                  sock.close()
                  return
                
                if line == "left":
                    mouse.click(Button.left)

                elif line == "right":
                    mouse.click(Button.right)

                elif line == "SCROLL_UP":
                    mouse.scroll(0, 1)

                elif line == "SCROLL_DOWN":
                    mouse.scroll(0, -1)
                else:
                    try:
                        x, y = map(int, line.split(","))
                        mouse.position = (x, y)
                    except ValueError:
                        print("Invalid data received:", line)

    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        sock.close()
if __name__ == "__main__":
    main()
