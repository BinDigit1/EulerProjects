'''

'''

import time

import MathFunctions

start_time = time.time()

for i in range(1, 10000):
    for j in range(10000, 1, -1):
        first_pentagon = MathFunctions.pentagonal(i)
        second_pentagon = MathFunctions.pentagonal(j)
        if (MathFunctions.inverse_pentagonal(abs(first_pentagon-second_pentagon)) and MathFunctions.inverse_pentagonal(first_pentagon+second_pentagon)):
            print(abs(first_pentagon-second_pentagon))

print("--- %s seconds ---" % (time.time() - start_time))