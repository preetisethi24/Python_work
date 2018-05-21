def findUnsortedSubarray(nums):
    print [a==b for a,b in zip(nums, sorted(nums))]
    is_same = [a == b for a, b in zip(nums, sorted(nums))]
    print is_same
    if all(is_same):
        return 0
    else:
        return len(nums)-is_same.index(False)-is_same[::-1].index(False)


print(findUnsortedSubarray([2,6,4,8,10,9,15]))
    
