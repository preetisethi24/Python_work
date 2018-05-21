n = int(raw_input("enter no of values").strip())
arr = [int(arr_temp) for arr_temp in raw_input("Enter the value").strip().split(' ')]
print " " .join(map(str,arr[::-1]))
