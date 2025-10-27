#קריאת הקובץ והשמה ברשימה
with open('fileFor_Frequency.txt', 'r') as file:
    words = file.read().split()
#כל מילה בקובץ הופכת למפתח במילון
wordsDict={}
for word in words:
    wordsDict[word]=0
## ספירת כמות הפעמים שכל מילה בקובץ מופיעה
for word in words:
    wordsDict[word]=wordsDict[word]+1
##רשימה ממוינת לפי הערך
sortedList=sorted(wordsDict.items(), key=lambda item: item[1], reverse=True)
