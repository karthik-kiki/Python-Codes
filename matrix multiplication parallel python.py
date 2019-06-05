import numpy as np
import threading
import time
start_time=int(round(time.time()*1000))
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[9,8,7],[6,5,4],[3,2,1]])
mul=(a.dot(b)).tolist()
print(mul)
print("Execution Time of sequential --->", (int(round(time.time() * 1000)) - start_time))
mux=[]
class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
    def run(self):
        print ("Starting " + self.name + "\n")
        c=(a[0].dot(b)).tolist()
        mux.append(c)
        print ("End " + self.name + "\n")
class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
    def run(self):
        print ("Starting " + self.name + "\n")
        d=(a[1].dot(b)).tolist()
        mux.append(d)
        print ("End " + self.name + "\n")
class Thread3(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
    def run(self):
        print ("Starting " + self.name + "\n")
        e=(a[2].dot(b)).tolist()
        mux.append(e)
        print ("End " + self.name + "\n")
start = int(round(time.time() * 1000))

thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

print("Execution Time of threads--->", (int(round(time.time() * 1000)) - start))
print(mux)
        
        
