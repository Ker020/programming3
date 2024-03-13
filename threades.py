import time
import threading

def kero(number):
    for n in number :
        print(n*n,time)
def koko(number):
    for n in number:
        print (n*n*n,time)
arr=[2,3,4,5]
t=time.time
t1=threading.Thread(target=kero,args=(arr,))
t2=threading.Thread(target=koko,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("done",time.thread_time())