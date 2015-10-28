'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''
from math import sqrt
import time

start_time = time.time()

UPPER_LIMIT = 600851475143
my_primes = []
x=3
while(x<UPPER_LIMIT//2):

    if (UPPER_LIMIT%x ==0):
        print("Potential prime: ", x)
        #potential prime - check with previous primes in set
        is_prime = True
        for prime in my_primes:
            if (prime>x//2):
                break
            elif (x%prime == 0):
                is_prime = False
                break

        if (is_prime):
            my_primes.append(x)
            print("added prime: ", x)
    x+=2

print(my_primes)

print("--- %s seconds ---" % (time.time() - start_time))
