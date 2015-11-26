"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import MathFunctions
import time, unittest


def prime_counter(order_in_primes):
    current_num = 2
    current_order_in_primes = 0
    while True:
        if MathFunctions.checkIfPrime(current_num):
            current_order_in_primes += 1
        if current_order_in_primes < order_in_primes:
            current_num += 1
        else:
            break
    return (current_num)


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_counter(6), 13)


start_time = time.time()
print(prime_counter(10001))
print("--- %s seconds ---" % (time.time() - start_time))
