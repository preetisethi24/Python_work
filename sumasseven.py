def sortedarray(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==7-arr[j]:
                return arr[i],arr[j]


print(sortedarray([2,3,4]))
