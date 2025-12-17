import socket
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

def uploadFile():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8080))
    path = filedialog.askopenfilename(title="Choose a file")
    if path:
        filename = os.path.basename(path)
        sock.send("uploadFile".encode())
        sock.send(filename.encode())
        with open(path, "rb") as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                sock.send(chunk)
        messagebox.showinfo("Success", "File uploaded successfully!")
    sock.close()

def downloadFile():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8080))
    filename = simpledialog.askstring("Download", "Enter file name:")
    if filename:
        sock.send("downloadFile".encode())
        sock.send(filename.encode())
        with open("downloaded_" + filename, "wb") as f:
            while True:
                chunk = sock.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
        messagebox.showinfo("Success", "File downloaded successfully!")
    sock.close()


root = tk.Tk()
root.title("File Transfer")
root.geometry("350x220")
root.resizable(False, False)
title = tk.Label(root, text="File Transfer App", font=("Arial", 16))
title.pack(pady=10)
send_btn = tk.Button(root, text="Upload File", command=uploadFile, width=20)
send_btn.pack(pady=5)
download_btn = tk.Button(root, text="Download File", command=downloadFile, width=20)
download_btn.pack(pady=5)

root.mainloop()
