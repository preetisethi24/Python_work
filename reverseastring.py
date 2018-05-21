def reverseastring(string):
    l=[]
    count=1
    for c in range(0,len(string)):
        l.append(string[len(string)-count])
        count=count+1
    return "".join(l)
print(reverseastring("preeti"))
        
        
