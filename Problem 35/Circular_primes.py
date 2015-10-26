'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''
from MathFunctions import checkIfPrime
import time
def isCircularPrime(number):
    length = len(str(number))
    if (length==1):
        return checkIfPrime(number)

    else:
        for variation in list_of_variations(number):
            if not checkIfPrime(variation):
                return False
        return  True


def list_of_variations(number):
    tempList =[]
    tempList.append(number)
    stringRep = str(number)
    if(len(stringRep)>1):
        for i in range(len(stringRep)-1):
            stringRep = stringRep[1:]+stringRep[:1]
            tempList.append(int(stringRep))

    return tempList

start_time = time.time()
number_of_primes = 0
for i in range(2, 1000000):
    if(i>2):
        strRep = str(i)
        # optimisation - skip numbers that contain even digits
        if ('2' in strRep or '4' in strRep or '6' in strRep or '8' in strRep or '0' in strRep):
            continue

    if isCircularPrime(i):
        number_of_primes+=1
print(number_of_primes)
# print(list_of_variations(1978))
print("--- %s seconds ---" % (time.time() - start_time))
