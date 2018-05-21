class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    #insert at the end of the linkedList
    def append(self,data):
        new_Node=Node(data)
        if self.head==None:
           self.head=new_Node
           return

        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_Node

    #insert at the start fo he LinkedList
    def push(self,data):
        new_Node=Node(data)
        new_Node.next=self.head
        self.head=new_Node

    #insert after a given previous Node
    def insertAfter(self,prevNode,data):
        if prevNode is None:
            print"Previous Node deosnt exist int he LinekdList"
            return
        new_Node=Node(data)
        new_Node.next=prevNode.next
        prevNode.next=new_Node

    def count(self):
        total=0
        current=self.head
        while current!=None:
            total+=1
            print "data is",current.data
            current=current.next
        print"Count is", total
        return total

    def printList(self):
        if self.head==None:
            print "List is empty"
        current=self.head
        while(current):
            print current.data
            current=current.next

    def printmidelement(self,mid):
        current=self.head
        i=0
        while(i<mid):
            current=current.next
            i+=1
        print"middle node is ",current.data
llist=LinkedList()
llist.printList()
llist.push(0)
llist.push(1)
llist.push(6)
llist.append(2)
llist.append(3)
llist.append(4)
llist.printList()
llist.insertAfter(llist.head,8)
print"New list now is:"
llist.printList()
total=llist.count()
print"middle element is at position",total/2
llist.printmidelement(total/2)
