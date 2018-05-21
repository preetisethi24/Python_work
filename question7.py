def question7():
    input_str=raw_input("enter no of rows and coloums:")
    input=[int(x) for x in input_str.split(",")]
    row=input[0]
    col=input[1]
    l=[[0 for x in range(col)] for y in range(row)]
    print l
    for x in range(row):
        for y in range(col):
            l[x][y]=x*y
    print l
                    
question7()
