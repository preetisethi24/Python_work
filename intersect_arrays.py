import collections
##def intersect(nums1, nums2):
##    a, b = map(collections.Counter, (nums1, nums2))
##    print a,b
##    print a&b
##    return list((a & b).elements())
##
##print(intersect([1,2,2,1],[2,2]))

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print c1
print c2

print list((c1 & c2).elements())
    
