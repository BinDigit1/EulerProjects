__author__ = 'kostakis'
'''
A 10-substring of a number is a substring of its digits that sum to 10. For example, the 10-substrings of the number 3523014 are:

3523014
3523014
3523014
3523014
A number is called 10-substring-friendly if every one of its digits belongs to a 10-substring. For example, 3523014 is 10-substring-friendly, but 28546 is not.

Let T(n) be the number of 10-substring-friendly numbers from 1 to 10n (inclusive).
For example T(2) = 9 and T(5) = 3492.

Find T(1018) mod 1 000 000 007.
'''
from math import pow
import time
import re

global start_time


def is10substring(number):
    return sumOfNums(number) == 10


def sumOfNums(number):
    sum = 0
    for c in number:
        sum += int(c)
    return sum


def isFriendly(number):
    number = re.sub('0', '', number)
    if sumOfNums(number)<10:
        return False


    length = len(number)
    friendlyValues = [False] * length

    for step in range(2, length + 1 if length < 11 else 10):
        currentindex = 0
        while currentindex + step <= length:
            currentSubstring = number[currentindex:currentindex + step]
            if (is10substring(currentSubstring)):
                # print(number, currentSubstring, friendlyValues, step)
                friendlyValues[currentindex: currentindex + step] = [True] * step
                # print(friendlyValues)
            currentindex += 1
            # if not(False in friendlyValues):
            #     return True

    isFriendly = True
    if (False in friendlyValues):
            isFriendly = False

    return isFriendly


def numberOf10Friendly(n):
    number = 0
    global start_time

    for x in range(9, int(pow(10, n)) + 1):
        # if isFriendly(re.sub('0', '', str(x))):

        if isFriendly(str(x)):
            number += 1
            # if (number % 1000000007 == 0):
            #     print("found number ", number)
            #     print("--- %s seconds ---" % (time.time() - start_time))
    return number


start_time = time.time()
# print(numberOf10Friendly(2))
# print(numberOf10Friendly(5))
# print("--- %s seconds ---" % (time.time() - start_time))
print(numberOf10Friendly(18) % 1000000007)
print("--- %s seconds ---" % (time.time() - start_time))
