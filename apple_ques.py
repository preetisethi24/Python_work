def find_glitch(a_list):
    while(len(a_list)>=1):
        l=[]
        b=[]
        for i in range(len(a_list)+1):
            print "a_list is",len(a_list)
            l.append(a_list[i])
            for j in range(i+1,len(a_list)+1):
                print"Value of i and j is",i,j
                if a_list[i]>=a_list[j]-1:
                    l.append(a_list[j])
                    print l
                    if len(l)>1:
                        b.append(l[0])
                        print b
                else:
                    del a_list[0:len(l)]
                    
    
                 

find_glitch([1.01,1.05,1.07,2.01,2.075,3.0])
                
                   
                   
    
