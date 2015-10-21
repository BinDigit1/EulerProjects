__author__ = 'k.vasileiou'
import math

def checkIfPrime(i):
    if(i == 2):
        return True
    elif(i%2 == 0):
        return False
    else:
        isPrime = True
        for num in range(3,int(math.sqrt(i)+1)):
            #print(num)
            if(i%num == 0):
                isPrime = False
                break
        return isPrime