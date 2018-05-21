class Person(object):
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)



class Student(Person):
    def __init__(self,firstName,lastName,idNum,scores):
        super(Student,self).__init__(firstName,lastName,idNum)
        self.scores=scores

    def calculate(self):    
        average=sum(self.scores)/len(self.scores)
        if average>=90 and average<=100:
            return "O"
        elif average>=80 and average<=90:
            return "E"
        elif average>=70 and average<=80:
            return "A"
        elif average>=55 and average<=70:
            return "P"
        elif average>=40 and average<=55:
            return "D"
        else:
            return "T"

line = raw_input("enter the values").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, raw_input("enter the list").split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
