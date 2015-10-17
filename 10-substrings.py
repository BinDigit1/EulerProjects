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

def is10substring(number):
    return sumOfNums(number)==10


def sumOfNums(number):
    sum = 0
    for c in str(number):
        sum += int(c)
    return sum

'''returns all substrings of a string with length step'''
def substringizer(number, step):
    resultSet=list()
    length = len(number)
    currentIndex = 0
    while(currentIndex+step<=length):
        resultSet.append(number[currentIndex:currentIndex+step:])
        currentIndex+=1
    return resultSet

def getAllMySubstrings(number):
    resultSet=list()
    for i in range(2,len(number)-1):
        resultSet.append(substringizer(number, i))
    return resultSet


print(getAllMySubstrings(str(3523014)))
