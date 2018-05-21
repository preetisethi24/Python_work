def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)




n=int(raw_input("enter the number:"))
print factorial(n)


    
