def lengthoflastword(s):
    l=(s.strip(" ")).split(" ")
    print l
    if len(l)>0:
        return len(l[-1])
    else:
        return 0

print(lengthoflastword("a "))
    
    
