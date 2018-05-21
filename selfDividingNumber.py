def is_self_driving(num):
    for n in str(num):
        if n=='0' or num%int(n)!=0:
            return False
    return True

def selfDividingNumbers(left,right):
    l=[]
    for num in range(left,right+1):
        if is_self_driving(num):
            l.append(num)                
    return l

print(selfDividingNumbers(1,22))
                
