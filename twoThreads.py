import threading
count=0
def thread1():
    global count
    for i in range(100000):
        count=count+1
def thread2():
    global count
    for i in range(100000):
        count=count-1
t1=threading.Thread(target=thread1)
t2=threading.Thread(target=thread2)
t1.start()
t2.start()
t1.join()
t2.join()
print(count)