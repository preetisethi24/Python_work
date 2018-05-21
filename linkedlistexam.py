class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_Node

    def setNext(self,new_next):
        self.next_Node=new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head

    def insert(self,data):
        new_Node=Node(data)
        new_Node.setNext(self.head)
        self.head=new_Node
        return new_Node

    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.getNext()
        return count

l=LinkedList()
l.insert(2)
print l
