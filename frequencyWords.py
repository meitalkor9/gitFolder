#קריאת הקובץ והשמה ברשימה
with open('fileFor_Frequency.txt', 'r') as file:
    words = file.read().split()
#כל מילה בקובץ הופכת למפתח במילון
wordsDict={}
for word in words:
    wordsDict[word]=0
