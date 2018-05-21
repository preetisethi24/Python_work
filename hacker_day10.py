n = int(raw_input("Enter the nubmer").strip())
c=bin(n)[2:]
print c
a=str((bin(n)[2:])).split('0')
print a
b=max(map(len,a))
print b

