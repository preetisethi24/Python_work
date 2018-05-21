def question12():
    l=[]
    for num in range(1000,3000):
        s = str(num)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            l.append(s)
    print l
question12()
                    
                
        
    
