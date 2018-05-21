def maximumProduct1(l):
    l.sort()
    print l
    return max(l[-1]*l[-2]*l[-3],l[0]*l[1]*l[-1])
    
    
print(maximumProduct1([-4,-3,-2,-1]))
