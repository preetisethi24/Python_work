def removeElement(nums,val):    
    for num in nums:
        if num==val:
            nums.remove(val)
            print nums

    else:
        return len(nums)

print(removeElement([3,3],3))
