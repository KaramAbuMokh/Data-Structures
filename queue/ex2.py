import ex1
import time

q=ex1.queue()
q.enqueue('1')
print('1')
time.sleep(1)
while True:
    num=q.dequeue()
    q.enqueue(num+'0')
    print(num+'0')
    time.sleep(1)
    q.enqueue(num + '1')
    print(num + '1')
    time.sleep(1)
