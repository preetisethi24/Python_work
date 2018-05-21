
class Pets:
    dogs=[]

    def __init__(self,dogs):
        self.dogs=dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())
class Dog:
    #class attribute
    species='mammals'
    
    
    #Inititalizer/Instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.is_hungry=True

    #instance method
    def description(self):
        return self.age,self.name

    #instance method
    def speak(self,sound):
        self.sound=sound
        return "%s says %s",(self.name,sound)

    #instance method
    def eat(self):
        self.is_hungry=False

    def walk(self):
        return "%s is walking!"%(self.name)


#Child class inherits from Dog class
class BullDog(Dog):
    def run(self,speed):
        return "%s runs %s" % (self.name,speed)


#Child class inherits from Dog class
class RusselTerrier(Dog):
    def run(self,speed):
        return "%s runs %s" %(self.name,speed)

my_dogs=[BullDog("abc",12),RusselTerrier("xyz",14),Dog("lmn",34)]

my_pets=Pets(my_dogs)

my_pets.walk()

