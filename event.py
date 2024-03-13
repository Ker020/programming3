from threading import Thread,Event
from time import sleep
def task(event:Event,id:int):
    print(f'\nthis {id}started.wating')
    event.wait()
    print(f'\nrecived.this{id}completed')
def main():
     event=Event()
     t1=Thread(target=task,args=(event,1))
     t2=Thread(target=task,args=(event,2))
     t1.start()
     t2.start()
     print('blocking 3 second')
     sleep(3)
     event.set
if __name__ == "__main__":
        main()