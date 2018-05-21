def findnumbers(first,last):
    new_list=[]
    for num in range(first,last+1):
        if (num%7==0) and (num%5!=0):
            new_list.append(str(num))
    return ",".join(new_list)


print(findnumbers(2000,3200))
