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

class Developer(Employee):
    raise_amt=1.01
    def __init__(self,first,last,pay,prog_lan):
        Employee.__init__(self,first,last,pay)
        self.prog_lan=prog_lan

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_dev(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_dev(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
        
dev_1=Developer('Preeti','Sethi',1000,'Python')
dev_2=Developer('Viaan','Manocha',2000,'Java')

#print(dev_1.email)
#print(help(Developer))
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_1.email)
#print(dev_1.prog_lan)
Mgr_1=Manager("Sue","Freeman",90000,[dev_1])
print(Mgr_1.email)
Mgr_1.print_emp()
Mgr_1.add_dev(dev_2)
Mgr_1.print_emp()
Mgr_1.remove_dev(dev_1)
Mgr_1.print_emp()
