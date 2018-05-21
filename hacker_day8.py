n=int(raw_input("Enter how many"))
d={}
names=[]
for i in range(0,n):
    name=raw_input("enter the name")
    d[name]=int(raw_input("enter the phone number"))

try:
    while True:
        inp = raw_input("Enter the name to search")
        if inp != "":
            names.append(inp)
        else:
            break
except EOFError:
        pass

for name in names:
    if name in d:
        print("{}={}".format(name,d[name]))
        #print name,d[name]
    else:
        print "Not found"


    


