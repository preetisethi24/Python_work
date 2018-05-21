
def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    m=sorted(nums)
    n=len(m)
    if (len(nums)==0 or len(nums)==1):
            return 0
    else:
        for num in range(n-1):
            if 2*m[num]>m[n-1]:
                return -1
        else:
            return nums.index(max(nums))
print(dominantIndex([1,2,3]))
