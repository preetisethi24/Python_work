from numpy import reshape as np
def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """

    len_of_orig_mat=len(nums)*len(nums[0])
    len_of_output_mat=r*c
    if len_of_orig_mat!=len_of_output_mat:
        return nums
    else:
        print(type(np(nums,r*c).tolist()))
        return np(nums,r*c)


print(matrixReshape([[1,2],[3,4]],1,4))
                                  
