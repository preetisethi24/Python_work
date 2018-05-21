#creating a class for car
class Car:

    #initialization and creating properties
    def __init__(self, licenseNum):
        self.licenseNum = licenseNum
        self.moveCount = 0

    #increase the moveCount by 1
    def move(self):
        self.moveCount += 1

    #get information to a string
    def toString(self):
        return "Car {0}\tmoves:{1}".format(self.licenseNum, self.moveCount)


#creating queue class for cars
class CarQueue:

    #initialization
    def __init__(self):
        self.carList = []

    #add car to the queue
    def enqueue(self, car):
        self.carList.append(car)

    #remove car from the queue
    def dequeue(self):
        return self.carList.pop(0)

    #return the car by license plate number
    def getCar(self, licenseNum):
        for car in self.carList:
            if car.licenseNum == licenseNum:
                return car

    #check whether license plate number is in the car list or not
    def contains(self, licenseNum):
        return self.getCar(licenseNum)!=None

    #remove car from the list   
    def remove(self, car):
        if self.contains(car.licenseNum):
            self.carList.remove(car)

    #return the number of cars in the list  
    def size(self):
        return len(self.carList)

    #check whether list is empty of not
    def isEmpty(self):
        return self.size()==0

    #return the index of the car in the list
    def positionOf(self, car):
        return self.carList.index(car)

    #move forward all the cars in southern side of the position.
    def moveCarsFrom(self, position):
        for c in self.carList[position:]:
            c.move()

    #get information to a string
    def toString(self):
        carNameList = []
        for car in self.carList:
            carNameList.append(car.licenseNum)
        return "[{0}]".format(" ".join(carNameList))


#creating class for the garage
class Garage:

    #initialization with the given number of rooms in the garage
    def __init__(self, maxSize):
        self.carQueue = CarQueue()
        self.maxSize = maxSize

    #add car to the list, when arrive
    def arrive(self, car):
        self.carQueue.enqueue(car)

    #remove car from the list and record movements of other cars to the southern side, when depart
    def depart(self, car):
        position = self.carQueue.positionOf(car)
        self.carQueue.remove(car)
        self.carQueue.moveCarsFrom(position)

    #check whether the garage is full or not
    def isFull(self):
        return self.carQueue.size()==self.maxSize



#create new garage which can hold up to 10 cars
garage = Garage(10)

#create new CarQueue to store waiting cars
waiting = CarQueue()

header = """
##############################################
               PARKING GARAGE
##############################################
Welcome!
"""

help = """
you have to input your command and press enter.
[a/d] [LICENSE PLATE NUMBER],   for car arrival or departure
    a,  arrival
    d,  departure

help,   show instructions
exit,   quit the programme
show,   show the queues in the garage and the waiting line
"""

#display the header
print("{0}Instructions:{1}\nPlease enter the command...".format(header, help))

#infinity loop to get user inputs again and again
while True:

    #get user command
    command = raw_input("\nlaughs> ")

    #excecuting general commands
    if command=="exit":
        print("Good bye!\n")
        break
    elif command=="help":
        print(help)
        continue
    elif command=="show":
        print("Garage        {0}: {1}".format(garage.carQueue.size(), garage.carQueue.toString()))
        print("Waiting line  {0}: {1}".format(waiting.size(), waiting.toString()))
        continue

    #get seperately the action character ('a' or 'd') and the license plate number from the command
    action = ""
    licenseNum = ""
    try:
        action,licenseNum = command.split()
    except:
        #show error message for invalid inputs
        print("Invalid input! Try again. Enter 'help' for instructions")
