def question15(num):
    n1=int("%s" %num)
    n2=int("%s%s" %(num,num))
    n3=int("%s%s%s" %(num,num,num))
    n4=int("%s%s%s%s" %(num,num,num,num))
    val=n1+n2+n3+n4
    print val

question15(9)
