n=int(raw_input("enter no of inpouts:"))
for i in range(0,n):
    even=[]
    odd=[]
    a_string=raw_input("enter the string:")
    for i in range(len(a_string)):
        if i%2==0:
            even.append(a_string[i])
        else:
            odd.append(a_string[i])
    print("".join(even)+" "+"".join(odd))
