def question11(numbers):
    l=[]
    num= [n for n in numbers.split(",")]
    for i in num:
        intp=int(i,2)
        if (intp%5==0):
            l.append(i)
    print ",".join(l)

question11("0000,1111,1100,0011")
