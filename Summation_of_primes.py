'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
from math import sqrt
import time


def checkIfPrime(i):
    if(i == 2):
        return True
    elif(i%2 == 0):
        return False
    else:
        isPrime = True
        for num in range(3,int(sqrt(i)+1)):
            #print(num)
            if(i%num == 0):
                isPrime = False
                break
        return isPrime

def sumOfPrimesBelow(upperLimit):
    sum = 0
    for i in range(2, upperLimit):
        if checkIfPrime(i):
            sum+=i
    return sum

start_time = time.time()
print(sumOfPrimesBelow(2000000))
print("--- %s seconds ---" % (time.time() - start_time))