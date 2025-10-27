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
##הדפסת המילים הנפוצות
import sys
try:
    N = int(sys.argv[1])
    for i in range(1,N+1):
        print(i,"- word",sortedList[i-1][0]," ",sortedList[i-1][1]," times")
        
except ValueError:
    print("Error: הפרמטר שהוזן אינו מספר")
    sys.exit(1)
except IndexError:
    print("Error: לא קיימים כל כך הרבה מילים בקובץ")
    sys.exit(1)