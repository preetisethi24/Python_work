def countPrimeSetBits(L, R):
    """
    :type L: int
    :type R: int
    :rtype: int
    """
    def isPrime(count):
        if count<2:
                return False
        else:
            for m in range(2,count):
                if count%m==0:
                    return False
            else:
                    return True
    num_of_prime=0
    for num in range(L,R+1):
        count=bin(num).count('1')
        if isPrime(count):
            num_of_prime+=1
    return num_of_prime
        
#print isPrime(7)
print(countPrimeSetBits(10,15))
