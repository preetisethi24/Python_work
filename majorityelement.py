import operator
def majorityElement(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print d
    l=sorted(d.items(),reverse=True,key=operator.itemgetter(1))
    print l
    for k,v in l:
        if v>len(nums)/2:
            print k

majorityElement([1])
