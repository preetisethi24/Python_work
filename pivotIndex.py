def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
     """
    if (len(nums))==0:
            return -1
    else:
        for num in range(1,len(nums)-1):
            if (sum(nums[0:num])==sum(nums[num+1:])):
                return nums.index(nums[num])
        else:
            return -1

print(pivotIndex([]))
