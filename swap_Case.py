def swap_case(s):
    l=[]
    for c in s:
        if c.islower():
            l.append(c.upper())
        else:
            l.append(c.lower())       
    return "".join(l)

print(swap_case("Hello"))
