#קריאת הקובץ והשמה ברשימה
with open(r"C:\Users\adamr\Documents\gitFolder\fileFreq.txt", "r", encoding="utf-8") as file:
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
    print("enter num")
    sys.exit(1)
except IndexError:
    print("there are no so much words")
    sys.exit(1)
#python C:\Users\adamr\Documents\gitFolder\frequencyWords.py 2