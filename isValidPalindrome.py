def isValidPalindrome(s):
    s = filter(str.isalnum, s.lower())
    print s
    stack=[]
    queue=[]
    for c in s:
        stack.append(c)
        queue.insert(0,c)
    print stack
    print queue
    print len(s)//2
    for i in range(len(s)//2):
        print stack.pop()
        print queue.pop()
        if stack.pop()!=queue.pop():
            return False
    else:
        return True
            

print(isValidPalindrome("M,adam"))
        
