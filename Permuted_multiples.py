'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import time
def checkSameDigits(number1, number2):
    strRep1 = set(str(number1))
    strRep2 = set(str(number2))
    return len(strRep2.difference(strRep1))==0

start_time = time.time()
i = 1
while(True):
    if(checkSameDigits(i, 2*i) and checkSameDigits(i, 3*i) and checkSameDigits(i,4*i) and checkSameDigits(i, 5*i) and checkSameDigits(i, 6*i)):
        break
    else:
        i+=1
print(i)
print("--- %s seconds ---" % (time.time() - start_time))