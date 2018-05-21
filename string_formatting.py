def string_formatting(n):
    w=len(bin(n)[2:])
    for i in range(1,n+1):
        print (str(i).rjust(w,' '),str(oct(i)[1:]).rjust(w,' '),str(hex(i)[2:]).capitalize().rjust(w,' '),str(bin(i)[2:]).rjust(w,' ')))

string_formatting(11)


    
    
