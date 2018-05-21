class Dog:

    species='mammam'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age


a=Dog("abc",8)
b=Dog("xyz",3)
c=Dog("lmn",10)

def get_oldest_number(*args):
    return max(args)

print " The oldest dog is {} years old".format(get_oldest_number(a.age,b.age,c.age))
