class Employee:
    
    no_of_employee=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first + '.' + last + '@' + 'email.com'
        self.pay=pay
        Employee.no_of_employee+=1

    def __repr__(self):
        return("Employee: {}, {} ".format(self.fullname(),self.email))
    def __str__(self):
        return'{}-{}'.format(self.fullname(),self.email)
        
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount


Emp_1=Employee("Preeti","Sethi",1000)
#print(Emp_1)
