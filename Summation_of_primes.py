'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import time, MathFunctions




def sumOfPrimesBelow(upperLimit):
    sum = 2
    for i in range(3, upperLimit, 2):
        if MathFunctions.checkIfPrime(i):
            sum+=i
    return sum

start_time = time.time()
print(sumOfPrimesBelow(2000000))
print("--- %s seconds ---" % (time.time() - start_time))