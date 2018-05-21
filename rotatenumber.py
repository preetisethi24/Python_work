def isValidNumber(s):
    print s
    return not(any(s in {'3','4','7'} for i in s))and(any(s in {'2','5','6','9'} for i in s))


def rotatenumber(nums):
    for num in range(1,nums+1):
        isValidNumber(str(num))
    return sum(isValidNumber(str(num)))

rotatenumber(11)
