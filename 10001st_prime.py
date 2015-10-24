"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import sqrt
from MathFunctions import checkIfPrime
import time


def primeCounter(orderInPrimes):
    currentNum = 2
    currentOrderInPrimes = 0
    while True:
        if checkIfPrime(currentNum):
            currentOrderInPrimes += 1
        if currentOrderInPrimes < orderInPrimes:
            currentNum += 1
        else:
            break
    print(currentNum)


start_time = time.time()

primeCounter(10001)
print("--- %s seconds ---" % (time.time() - start_time))
