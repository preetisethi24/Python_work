def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    d=dict()
    for c in candies:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    sum=0
    for k in d:
        if d[k]%2!=0:
            break
        else:
            return len(d.keys())

print (distributeCandies([1,1,2,3]))
