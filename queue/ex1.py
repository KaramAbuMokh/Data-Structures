import random
from collections import deque
import threading
import time

class queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,item):
        self.buffer.appendleft(item)

    def dequeue(self):
        if self.size()==0:
            return None
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        if self.size()==0:
            return True
        else:
            return False
    def prnt(self):
        str=''
        for item in self.buffer:
            str+=item+'-'
        print(str)


q=queue()
orders = ['pizza','samosa','pasta','biryani','burger']
def place_order():
    while True:
        i=random.randint(0,4)
        order=orders[i]
        q.enqueue(order)
        q.prnt()
        time.sleep(0.5)

def serve_order():
    while True:
        order=q.dequeue()
        q.prnt()
        print(f'served : {order}')
        time.sleep(2)

if __name__ == '__main__':
    Place_Order=threading.Thread(target=place_order)
    Place_Order.start()
    time.sleep(1)
    Serve_Order = threading.Thread(target=serve_order)
    Serve_Order.start()