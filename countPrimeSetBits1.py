import math
def countPrimeSetBits1(L, R):
    num_of_prime=0
    for num in range(L,R+1):
        count=bin(num).count('1')
        print("check for",count)
        if (count>2 and count%2==0):
            num_of_prime+=0
        else:
            for m in range(3,int(math.sqrt(count))+1):
                if (count%m)==0:
                    num_of_prime+=0
                else:
                    num_of_prime+=1
                    print("no of primes is",num_of_prime)
    return num_of_prime

print(countPrimeSetBits1(10,15))
