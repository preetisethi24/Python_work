def reverseInteger(n):
    s=cmp(n,0)
    print s
    r=int(str(abs(n))[::-1])
    print r
    if r<2**31:
        print s*r
    else:
        print 0


reverseInteger(-123)
