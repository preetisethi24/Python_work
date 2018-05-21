def question10(words):
    l=[]
    for word in words.split(" "):
        l.append(word)
        m= sorted(set(l))
    print " ".join(m)

question10("hello world again hello world hi")
    
    
