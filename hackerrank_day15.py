import collections
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None 

class SingleLinkedList:
    def __init__(self):
        self.head=Node()
    
    def display_list(self):
        if self.head is None:
            print "List is empty"
            return
        else:
            current = self.head
            while current.next!=None:
                print current.data
                current = current.next
    def count_list(self):
        total=0
        current=self.head
        while current.next!=None:
            total+=1
            current = current.next
        print"Total is: %d" % total

    def search_list(self,value):
        position=1
        current=self.head
        while current.next!=None:
            if current.data==value:
                print "Found at %d" %position
                return True
            current=current.next
            position+=1
                
        else:
            print "Not found in the list"
            return False

    def insert_at_start(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp


    def insert_at_end(self,data):
        temp=Node(data)
        if self.head is None:
           self.head=temp
           return

        current=self.head
        while current.next is not None:
            current=current.next
        current.next=temp

    def create_list(self):
        n=int(raw_input("enter the number of nodes:"))
        if n==0:
            return
        for i in range(n):
            data=int(raw_input("Enter the data ement to be inserted"))
            self.insert_at_end(data)

    def insert_after(self,data,x):
        current=self.head
        while current is not None:
            if current.data==x:
                break
            current=current.next
        if current is None:
            print(x,"not present in the list")
        else:
            temp=Node(data)
            temp.next=current.next
            current.next=temp


    def isPalindrome(self):
        queue = collections.deque([])
        cur = self.head
        while cur:
            queue.append(cur)
            cur = cur.next
        while len(queue) >= 2:
            if queue.popleft().data != queue.pop().data:
                return False
        return True

my_list=SingleLinkedList()

my_list.create_list()

while True:
    option=int(raw_input("Enter your option:"))
    if option==1:
        my_list.display_list()
    elif option==2:
        my_list.count_list()
    elif option==3:
        data=int(raw_input("Enter the element to be serached"))
        my_list.search_list(data)
    elif option==4:
        elem=int(raw_input("Enter the element to be inserted at beginning"))
        my_list.insert_at_start(elem)
    elif option==5:
        elem=int(raw_input("Enter the element to be inserted at end"))
        my_list.insert_at_end(elem)
    elif option==6:
        data=int(raw_input("Enter the data to insert"))
        elem=int(raw_input("Enter the element after which to insert"))
        my_list.insert_after(data,elem)
    elif option==7:
        print(my_list.isPalindrome())
            
    else:
        print "Not a valid input"
        break
        
            
