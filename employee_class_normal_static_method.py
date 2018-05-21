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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    #class method as alternative constructor
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_1_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def isworkday(day):
        if day.weekday==5 or day.weekday==6:
            return False
        return True

emp_A=Employee('Preeti','Sethi',1000)
emp_B=Employee('Viaan','Manocha',2000)

emp_1_str='preeti-Sethi-1000'
emp_2_str='viaan-Manocha-2000'

new_emp_1=Employee.from_string(emp_1_str)

Employee.set_raise_amt(1.05)
print(emp_A.raise_amt)
print(emp_B.raise_amt)
print(Employee.raise_amt)

import datetime
my_date=datetime.date(2016,7,10)

print(Employee.isworkday(my_date))
