import re
def fun(s):
    # return True if s is a valid email, else return False
    #a=re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    a=re.match(r'[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    #a=re.match(r'^[a-zA-Z][\w-]+@[\w]+\.[a-zA-Z]{1,3}$',s)
    return a
