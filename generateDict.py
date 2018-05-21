def generateDict(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

x=int(raw_input("Enter the integer:"))
print(generateDict(x))
