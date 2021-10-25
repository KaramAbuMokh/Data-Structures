'''
1 - create class for linked list
2- create class for nodes
3- function to insert to the head
4- function to print all elements
5- function to add to the end
6- function to insert list of elements
7- return the length of the linked list
8- remove element at index
9- insert element at index
10- insert_after_value
11- Remove first node that contains data
'''

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class List:
    def __init__(self):
        self.head=None
        self.tail = None

    def insert_head(self,data):
        if self.head==None:
            node = Node(data=data, next=None, prev=None)
            self.head = node
            self.tail = node
            return

        node = Node(data=data,next=self.head,prev=None)
        self.head.prev=node
        self.head=node
        return

    def prnt(self):
        el=self.head
        st=''
        while el:
            st+=str(el.data)+'---'
            el=el.next
        print(st)

    def prnt_backward(self):
        el=self.tail
        st=''
        while el:
            st+=str(el.data)+'---'
            el=el.prev
        print(st)

    def add_to_end(self,data):
        if self.head==None:
            self.insert_head(data)
            return
        last=self.tail
        node=Node(data,None,last)
        last.next=node
        self.tail=node
        return

    def insert_list(self,dataList):
        for data in dataList:
            self.add_to_end(data)

    def length(self):
        el=self.head
        cnt=0
        while el !=None:
            cnt+=1
            el=el.next
        return cnt

    def remove(self,i):
        if i<0 or i>self.length()-1:
            print('invalid index')
            return
        if self.length()==1:
            self.head=None
            self.tail=None
        if i==0:
            self.head=self.head.next
            self.head.prev=None
            return
        if i==self.length()-1:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        el=self.head
        cnt=0
        while cnt<i:
            cnt+=1
            el=el.next
        el.next.prev=el.prev
        el.prev.next=el.next
        return

    def insert_to_index(self,i,data):
        if i<0 or i>self.length():
            print('invalid index')
            return

        if i==0:
            node=Node(data,self.head,None)
            self.head.prev=node
            self.head=node
            return

        if i==self.length():
            node=Node(data,None,self.tail)
            self.tail.next=node
            self.tail=node
            return

        el = self.head
        cnt = 0
        while cnt < i - 1:
            cnt += 1
            el = el.next
        node=Node(data,el.next,el)
        el.next = node
        el.next.next.prev=node
        return

    def insert_after_value(self, data_after, data_to_insert):
        if self.tail.data==data_after:
            node = Node(data_to_insert, None, self.tail)
            self.tail.next = node
            self.tail = node
            return
        el = self.head
        while el!=None and el.data!=data_after  :
            el=el.next
        if el==None:
            print('data_after isnt in the list')
            return
        node=Node(data_to_insert,el.next,el)
        el.next=node
        el.next.next.prev=node
        return

    def remove_by_value(self, data):
        if self.head.data==data and self.tail.data==data and self.length()==1:
            self.head=None
            self.tail = None
            return
        if self.head.data==data:
            self.head=self.head.next
            self.head.prev=None
            return
        if self.tail.data==data:
            self.tail=self.tail.prev
            self.tail.next=None
            return
        el = self.head
        while el.next != None and el.next.data != data:
            el = el.next
        if el.next == None:
            print('data isnt in the list')
            return

        el.next = el.next.next
        el.next.prev=el
        return

if __name__ == '__main__':
    ll=List()
    ll.prnt()
    ll.insert_head(3)
    ll.insert_head(data=4)
    ll.insert_head(data=5)
    ll.prnt()
    ll.add_to_end(7)
    ll.prnt()
    ll.prnt_backward()

    ll.insert_list([55,66,99,88,77,41])
    ll.prnt()
    print(ll.length())

    ll.remove(0)
    ll.prnt()

    ll.insert_to_index(0,999)
    ll.prnt()
    ll.insert_after_value(41,111)
    ll.prnt()
    ll.remove_by_value(999)
    ll.prnt()