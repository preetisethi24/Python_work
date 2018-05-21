n = int(raw_input("Enter the num"))
arr = map(int, raw_input("enter the elements").split())
new_list=sorted(set(arr),reverse=True)[1]
print new_list
