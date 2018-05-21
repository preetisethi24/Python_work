n=int(raw_input("Enter the no:"))
def fib(n):
    # return a list of fibonacci numbers
    l=[]
    a,b=0,1
    for i in range(n):
        l.append(a)
        a,b=b,a+b       
    return l

fib(n)

cube=map(lambda x:x*x*x,fib(n))

print cube
