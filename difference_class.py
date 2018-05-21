class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        for element in self.__elements:
            print element


_ = raw_input("Enter the number")
a = [int(e) for e in raw_input("Enter now:").split(' ')]

d = Difference(a)
d.computeDifference()

#print(d.maximumDifference)
