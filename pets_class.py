
class Pets:
    dogs=[]

    def __init__(self,dogs):
        self.dogs=dogs
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

print "I have {} dogs.".format(len(my_dogs))

for dog in my_pets.dogs:
    print "{} is {}".format(dog.name,dog.age)

print"And they all are {},of course".format(dog.species)

are_my_dogs_hungry=False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry=True

if are_my_dogs_hungry:
    print("My dogs are hungry")
else:
    print("My dogs are not hungry")
        


