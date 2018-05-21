import operator
def findtopwords(filename5):
    a_list=[]
    d={}
    with open("preeti.txt","r") as f:
        for line in f:
            for word in line.strip("\n").split(" "):
                a_list.append(word)
        print a_list
        for word in a_list:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        #print sorted(d.items(),key=d.get,reverse=True)[:5]
        sorted_x = sorted(d.items(), key=operator.itemgetter(1),reverse=True)[:5]
        print sorted_x
        for k,v in sorted_x:
            print k
            
            





findtopwords("preeti.txt")
