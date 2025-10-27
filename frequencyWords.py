#קריאת הקובץ והשמה ברשימה
with open('fileFor_Frequency.txt', 'r') as file:
    words = file.read().split()