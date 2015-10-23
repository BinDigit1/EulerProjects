__author__ = 'k.vasileiou'
import math

def checkIfPrime(i):
    if(i == 2):
        return True
    elif(i%2 == 0):
        return False
    else:
        isPrime = True
        for num in range(3,int(math.sqrt(i)+1),2):
            #print(num)
            if(i%num == 0):
                isPrime = False
                break
        return isPrime

def triangular(number):
    return number*(number+1)/2

def inverse_triangular(number):
    delta = 1+8*number
    root = (-1 + math.sqrt(delta))/2

    return root==int(root)

def pentagonal(number):
    return number*(3*number-1)/2

def inverse_pentagonal(number):
    delta = 1+24*number
    root = (1 + math.sqrt(delta))/6

    return root==int(root)

def hexagonal(number):
    return number*(2*number - 1)

def inverse_hexagonal(number):
    delta = 1+8*number
    root = (1 + math.sqrt(delta))/4

    return root==int(root)

def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)