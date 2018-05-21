def plusOne(digits):
    l=[str(i) for i in digits]
    s= "".join(l)
    new_number= int(s)+1
    print [int(x) for x in str(new_number)]

plusOne([1,2,3,4])
