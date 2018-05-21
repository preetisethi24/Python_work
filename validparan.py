def validparanthesis(s):
    ls=[]
    d={")":"(","}":"{","]":"["}
    for c in s:
        if c in d.values():
            ls.append(c)
        elif c in d.keys():
            if (ls==[] or d[c]!=ls.pop()):
                return False
        else:
            return False
    return ls==[ ]
            
print(validparanthesis("{}"))
