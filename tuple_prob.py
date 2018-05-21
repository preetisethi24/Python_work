def tuple_prob(n,l):
    return hash(tuple(l))
##    t=( )
##    for i in range(1,n+1):
##        t=t+(i,)
##    return hash(t)

print(tuple_prob(5,[1,2,3,4,5]))
