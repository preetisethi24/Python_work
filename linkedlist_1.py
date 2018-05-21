class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total=0
        while cur_next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elem=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elem.appned(cur_node.data)
            
        print elem

my_list=LinkedList()
my_list.display()
        
