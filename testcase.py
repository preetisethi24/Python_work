def testcase():
    n=int(raw_input("Enter no of tetscases"))
    print(map(int,(raw_input("enter").split(" "))))
    for i in range(n):
        a,b=map(int,(raw_input("enter").split(" ")))
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print "Error code",e
        except ValueError as f:
            print "Error code",f


testcase()
