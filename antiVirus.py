import requests
import os
import threading
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
#המפתח שלי
API_KEY = "16e6e9a0ce5785fb7ec3434ed3003c35cb1b92349af0831ff7986cf38c9e8bad"
headers = {"x-apikey": API_KEY}

#פונקציה הסורקת את הקובץ
def uploadFile(filePath):
    #כתובת שבה אפשר לעלות קבצים לבדיקה
    url = "https://www.virustotal.com/api/v3/files"
    with open(filePath, "rb") as file:
        #יצירת מילון עם המפתח "file" והערך הוא האובייקט של הקובץ
        files = {"file": file}
        #שליחת בקשת POST ל-API של VirusTotal
        response = requests.post(url, files=files, headers=headers)
        result = response.json()#מחרוזת בפורמט מילון/רשימה
        if "data" not in result:
            print(f"Error uploading {filePath}: {result}")
            return None
        return result["data"]["id"]

global problems#כמות הקבצים החשודים
problems=0
#פונקציה המחזירה תשובה אם יש וירוס או לא בקובץ
def searchVirus(filePath):
    global problems
    file_id = uploadFile(filePath)
    if not file_id:
        return
    url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
    response = requests.get(url, headers=headers)#קבלת התוצאות
    data = response.json()
    if "data" not in data:#בדיקת תקינות התגובה
        print(f"Error analyzing {filePath}: {data}")
        return

    #מספר מנועי אנטי-וירוס שזיהו את הקובץ כמזיק (וירוס)
    malicious = data["data"]["attributes"]["stats"]["malicious"]
    #מספר מנועי אנטי-וירוס שזיהו את הקובץ כחשוד
    suspicious = data["data"]["attributes"]["stats"]["suspicious"]
    print("\nFile:", filePath)
    print("Malicious:", malicious)
    print("Suspicious:", suspicious)
    # עדכון ה-Label הקיים עם צבע לפי מצב
    if malicious > 0 or suspicious > 0:
        status = f"{filePath} → VIRUS"
        root.after(0, lambda: result_label.config(text=status, fg="red"))
        problems+=1
    else:
        status = f"{filePath} → CLEAN"
        root.after(0, lambda: result_label.config(text=status, fg="green"))
    root.update()

#פונקציה הבודקת תיקייה
def scanDirectory(start_path='./'):
    for root_dir, dirs, files in os.walk(start_path):#מעבר על כל הקבצים בתיקייה ותת-תיקיות
        if ".git" in root_dir or "venv" in root_dir or "__pycache__" in root_dir:
            continue
        for file in files:
            full_path = os.path.join(root_dir, file)#בניית נתיב לקובץ
            searchVirus(full_path)

#פתיחת חלון של סייר הקבצים
def start_scan():
    global problems
    problems = 0
    folder = filedialog.askdirectory(title="Choose folder")
    if folder:#אם נבחרה תיקייה תתחיל הסריקה
        scanDirectory(folder)
    root.after(0, lambda: result_label.config(
    text=f"Scan finished! {problems} damaged files were found",
    font=("David",15, "bold"),fg="purple",bg="plum"))

def start_scan_thread():
      threading.Thread(target=start_scan).start()
# GUI עיצוב
root = tk.Tk()#פתיחת חלון
root.geometry("800x500")#גודל
root.config(bg="plum")#צבע החלון

label1 = tk.Label(root, text="Welcome to my Anti Virus!", font=("David", 40, "bold"), fg="purple", bg="plum")
label1.pack(pady=50)

label2 = tk.Label(root, text="Click here to choose a folder", font=("David", 30), fg="pink", bg="purple", cursor="hand2")
label2.pack(pady=20)

# Label אחד לסטטוס
result_label = tk.Label(root, text="", font=("David", 12), bg="plum", fg="white")
result_label.pack(pady=20)

label2.bind("<Button-1>", lambda e: start_scan_thread())

# Image
pil_image = Image.open(r"C:\Users\adamr\Documents\gitFolder\virusDraw.png")
pil_image.thumbnail((150, 150))
img = ImageTk.PhotoImage(pil_image)
label3 = tk.Label(root, image=img)
label3.pack(pady=10)

root.mainloop()
