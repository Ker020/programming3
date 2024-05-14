import multiprocessing
def pro1(list,q):
    for num in list:
        q.put(num*num) 
def print_pro1(q):
    while not q.empty:
        print(q.get())
    print("queue isnt empty")
if __name__ == "__main__":
   list=[2,4,6]
   q=multiprocessing.Queue
   p1=multiprocessing.Process(target=pro1,args=(list,q))
   p2=multiprocessing.Process(target=print_pro1,args=(q,))
   p1.start
   p1.join
   p2.start
   p2.join
