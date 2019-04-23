def capitalize(string):
##    new_list=[]
##    words=string.split(" ")
##    for word in words:
##        new_list.append(word.capitalize())
##    return " ".join(new_list)
    return(" ".join(word.capitalize() for word in string.split(" "))) 

print(capitalize("chris sethi"))
print(capitalize("preeti sethi"))
