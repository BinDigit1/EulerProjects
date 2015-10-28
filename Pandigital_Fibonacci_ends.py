'''
Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

import time, MathFunctions
all_digits=set(['1','2','3','4','5','6','7','8','9'])

def first9pandigital(number):
    global all_digits
    return len(all_digits.difference(set(str(number)[:9])))==0
def last9pandigital(number):
    global all_digits
    return len(all_digits.difference(set(str(number)[-9:])))==0

start_time = time.time()
i = 1
while True:
    current_fib = MathFunctions.fib(i)
    # print(i, len(str(current_fib)))
    if first9pandigital(current_fib) and last9pandigital(current_fib):
        break
    i+=1

print(i)
print("--- %s seconds ---" % (time.time() - start_time))