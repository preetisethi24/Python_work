class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_Node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_Node


    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elems=[]
        cur_node=self.head
        while(cur_node.next!=None):
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print elems

    def get(self,index):
        if index>self.length():
            print "Error :'Get' Index out of range"
            return None
        cur_indx=0
        cur=self.head
        while True:
            cur=cur.next
            if cur_indx==index:
                return cur.data
            cur_indx+=1

    def erase(self,index):
        if index>self.length():
            print "Error: out of range"
            return None
        cur_indx=0
        cur_Node=self.head
        while True:
            last_Node=cur_Node
            cur_Node=cur_Node.next
            if cur_indx==index:
                last_Node.next=cur_Node.next
                return
            cur_indx+=1
                
my_list=LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print "Length of the list is %d" %my_list.length()
indx=(my_list.length())//2
print indx
print "the element at the mid if the list is %d" %my_list.get(indx)
##print "element at index :%d" % my_list.get(2)
##my_list.erase(1)
##my_list.display()
