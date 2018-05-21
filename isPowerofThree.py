def isPowerOfThree(n):
    sum=0
    while(n>0):
        remain=n%10
        print "remain is %d" %remain
        sum+=remain
        n=n//10
        print "number is %d" %n
    print sum
    if sum%3==0:
        return True
    else:
        return False

print(isPowerOfThree(33))
