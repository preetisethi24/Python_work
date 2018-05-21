def isPrime(n):
    if n<=1:
        print "Not a Prime no"
    for i in range(2,n):
        if n%i==0:
            print"Not a Prime no"
            break
    else:
        print"Prime no"


isPrime(3)
