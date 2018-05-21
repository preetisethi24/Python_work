def listtoFile(x):
    
    with open("myfile.txt","w") as f:
        for elem in x:
            f.write(elem+'\n')

listtoFile(["table", "chair", "cup", "fork"])
