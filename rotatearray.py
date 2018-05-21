def rotateArray(nums,k):
    b=[1,2,3,4,5]
    x=len(nums)-k
    nums[:]=nums[x:]+ nums[:x]
    print nums
    print b[:]
rotateArray([1,2,3,4,5,6,7],2)
