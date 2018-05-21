def firstUniqChar(s):
    for c in s:
        if s.count(c)==1:
            return s.index(c)
    else:
            return -1


print(firstUniqChar("loveleetcode"))
