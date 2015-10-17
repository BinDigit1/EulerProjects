'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
def checkIfPrime(i):
    isPrime = True
    for num in range(2,i//2+1):
        #print(num)
        if(i%num == 0):
            isPrime = False
            break
    return isPrime

def primeCounter(orderInPrimes):
    currentNum = 2
    listOfPrimes = list()
    while(len(listOfPrimes)<orderInPrimes):
        if(checkIfPrime(currentNum)):
            listOfPrimes.append(currentNum)
        currentNum+=1
    print(listOfPrimes[-1])



primeCounter(10001)