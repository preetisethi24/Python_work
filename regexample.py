import re
def question23():
    emailAddress = raw_input("enter the emailaddress:")
    pat2 = "(\w+)@((\w+)\.(com))"
    r2 = re.match(pat2,emailAddress)
    print re
    print r2.group(1),r2.group(2)

question23()
