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
import re
def is10substring(number):
    return sumOfNums(number)==10


def sumOfNums(number):
    sum = 0
    for c in str(number):
        sum += int(c)
    return sum


def isFriendly(number):
    number = re.sub('0', '', number)
    friendlyValues = [False]*len(number)
    resultSet=[]
    length = len(number)

    for step in range(2,length+1):
        currentIndex = 0
        while(currentIndex+step<=length):
            currentSubstring=number[currentIndex:currentIndex+step:]
            if(is10substring(currentSubstring)):
                #print(currentSubstring)
                for i in range(currentIndex,currentIndex+step):
                    friendlyValues[i]=True
            currentIndex+=1
    isFriendly = True
    for i in friendlyValues:
        if i==False:
            isFriendly=False
            break
    return isFriendly


def numberOf10Friendly(n):
    number = 0

    for x in range(9, int(pow(10,n))+1):
        if isFriendly(str(x)):
            number+=1
            if(number%10000 == 0):
                print("found number ",number)
    return number



print(numberOf10Friendly(18)%1000000007)