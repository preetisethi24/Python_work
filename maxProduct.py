def maximumProduct(l):
    first=max(l)
    l.remove(first)
    second=max(l)
    l.remove(second)
    third=max(l)
    return first*second*third
    
    
print(maximumProduct([6,2,3,6]))
