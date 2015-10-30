'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import MathFunctions

def is_pandigital():
    pass

for i in range(999999999, 0, -1):
    if MathFunctions.miller_is_prime(i):
        print(i)
        break

