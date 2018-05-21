def listtofile(filename):
    with open(filename,"r") as f:
        elements=[elem.strip("\n") for elem in f]
        print elements


listtofile("myfile.txt")
