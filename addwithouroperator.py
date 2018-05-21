def Add(x,y): 
    # Iterate till there is no carry 
    while (y != 0):
     
        # carry now contains common
        # set bits of x and y
        print bin(x)[2:]
        print bin(y)[2:]
        
        carry = x & y
        print carry
 
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y
        print bin(x)[2:]
        print x
 
        # Carry is shifted by one so that   
        # adding it to x gives the required sum
        y = carry << 1
     
    return x
 
print(Add(15, 30))

0010
0011
0001

1110
1101
