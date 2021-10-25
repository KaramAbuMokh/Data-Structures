'''
1- push
2- pop
3- peak ( top )
4- is empty
5- size
'''
from collections import deque
class stack:
    def __init__(self):
        self.container=deque()

    def push(self,item):
        self.container.append(item)

    def pop(self):
        if self.size()==0:
            return None
        return self.container.pop()

    def peak(self):
        if self.size==0:
            print('stack is empty')
            return None
        else:
            return self.container[-1]

    def size(self):
        return len(self.container)
    def is_empty(self):
        if self.size()==0:
            return True
        else:
            return False

    def reverse_elements(self):
        return [self.pop() for i in range(self.size())]
if __name__ == '__main__':
    s=stack()
    for i in "We will conquere COVID-19":
        s.push(i)
    print(s.container)
    str=''
    for i in range(len("We will conquere COVID-19")):
        str+=s.pop()
    print(str)