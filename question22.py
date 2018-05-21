def question22():
    d=dict()
    words=raw_input("enter the words:")
    for word in words.split():
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    words=d.keys()
    words.sort()
    for w in words:
        print ("%s:%d" %(w,d[w]))


question22()
