'''
Which starting number, under one million, produces the longest chain?
'''
import time
def Collatz(number):
    if number == 1:
        return 1
    elif number%2 == 0:
        return 1+ Collatz(number/2)
    else:
        return 1 + Collatz(3*number + 1)


start_time = time.time()
max_steps = 1
biggest_start = 1
for i in range(3,1000000,2):
    temp = Collatz(i)

    if temp>max_steps:
        max_steps = temp
        biggest_start = i
print(biggest_start)
print("--- %s seconds ---" % (time.time() - start_time))