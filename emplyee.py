class Employee:

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first + '.' + last + '@' + 'email.com'
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)



empl=Employee('Preeti','Sethi',1000)
emp2=Employee('Viaan','Manocha',2000)
print(emp1.fullname)
print(emp2.fullname)
    
