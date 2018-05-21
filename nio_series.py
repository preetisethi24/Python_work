def series(a,b,n):
    for i in range(n):
        if i==0:
            seq=a
        elif i==1:
            seq=b
        else:
            seq=a+b
            a=b
            b=seq
    return seq
            
            

print(series(2,1,6))
