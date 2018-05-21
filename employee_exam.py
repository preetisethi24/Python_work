class Employee:
    no_of_employee=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first + '.' + last + '@' + 'email.com'
        self.pay=pay
        Employee.no_of_employee+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        #pass
        
emp_A=Employee('Preeti','Sethi',1000)
emp_B=Employee('Viaan','Manocha',2000)
#print(emp_A.fullname())
#print(emp_B.fullname())
#print(Employee.no_of_employee)
#print(Employee.raise_amt)
#print(emp_A.raise_amt)
#print(emp_B.raise_amt)

print(emp_A.pay)
emp_A.apply_raise()
print(emp_A.pay)

print(emp_A.__dict__)
print(Employee.__dict__)

emp_A.raise_amt=1.05
print(emp_A.__dict__)

print(emp_A.raise_amt)
print(emp_B.raise_amt)
print(Employee.raise_amt)

print(emp_A.apply_raise())
print(emp_A.pay)

