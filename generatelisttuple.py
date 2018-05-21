def generatelisttuple(x):
    l=[]
    t=()
    l=x.split(",")
    t=tuple(l)
    print l
    print t

x=(raw_input("Enter the numbers:"))
generatelisttuple(x)
