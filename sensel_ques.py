
# Write the letters A to Z, one per line, to file a2z.txt.
# Write numbers 0 to 25, one per line, shuffled in random order to file numbers.txt
# Assume the files may have changed, but still contain lists of strings and integers.
# Read in both files and print the lines from file a2z.txt sorted by the numbers in file numbers.txt

from random import shuffle

with open("a2z.txt","w") as f1:
    for letter in range(65,91):
        f1.write(chr(letter)+'\n')
        
with open("numbers.txt","w") as f2:
    l=[i for i in range(0,26)]
    shuffle(l)
    for num in l:
        f2.write(str(num)+'\n')
    
with open("numbers.txt","r") as f2:
    with open("a2z.txt","r") as f1:
        numbers = [num.strip("\n") for num in f2]
        numbers=map(int,numbers)
        print numbers
        letters = [letter.strip("\n") for letter in f1]
        print letters
        for num in numbers:
            print(letters[num],num)
