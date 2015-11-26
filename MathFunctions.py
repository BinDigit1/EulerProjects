import random
import math, functools


def checkIfPrime(i):
    if i == 1:
        return False
    elif (i == 2):
        return True
    elif (i % 2 == 0):
        return False
    else:
        isPrime = True
        for num in range(3, int(math.sqrt(i) + 1), 2):
            # print(num)
            if (i % num == 0):
                isPrime = False
                break
        return isPrime


def triangular(number):
    return number * (number + 1) / 2


def inverse_triangular(number):
    '''
    Checks if a number is triangular, i.e. if there exists a natural n for which T(n) = number
    :param number: the number to be checked
    :return: true if the given number is triangular, false otherwise.
    '''
    delta = 1 + 8 * number
    root = (-1 + math.sqrt(delta)) / 2

    return root == int(root)


def pentagonal(number):
    return number * (3 * number - 1) / 2


def inverse_pentagonal(number):
    delta = 1 + 24 * number
    root = (1 + math.sqrt(delta)) / 6

    return root == int(root)


def hexagonal(number):
    return number * (2 * number - 1)


def inverse_hexagonal(number):
    delta = 1 + 8 * number
    root = (1 + math.sqrt(delta)) / 4

    return root == int(root)


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fast_fib(n):
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':    v1, v2, v3 = v1 + v2, v1, v2
    return v2


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def miller_is_prime(n, _precision_for_huge_n=16):
    if n in (0, 1):
        return False
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if miller_is_prime(x)]


def is_pandigital(num):
    set_of_num = set(i for i in str(num))
    set_of_all_digits = set(str(i) for i in range(1, len(str(num)) + 1))
    return len(str(num)) == len(set_of_num) and set_of_all_digits.difference(set_of_num) == set()
