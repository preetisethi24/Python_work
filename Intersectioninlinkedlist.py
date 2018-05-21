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

class Solution(LinkedList):
    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A

my_list1=LinkedList()
my_list2=LinkedList()

my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
my_list1.append(4)
my_list1.display()


my_list2.append(4)
my_list2.append(5)
my_list2.append(3)
my_list2.append(2)
my_list2.display()

a=Solution()
a.getIntersectionNode(my_list1,my_list2)
print a
