'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ? 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will
be formed. If this process is continued, what is the side length of the square spiral for which the ratio of
primes along both diagonals first falls below 10%?
'''
import time, MathFunctions

def diagonal_members(size):
    diagonals = set()
    for i in range(size, 0,-2):
        # print("Layer ", i)
        for j in range(0,4):
            # print(i, j, i*i - (i-1)*j)
            diagonals.add(i*i - (i-1)*j)
    number_of_primes = sum(1 for x in diagonals if MathFunctions.miller_is_prime(x))
    # print(number_of_primes,len(diagonals))
    return (number_of_primes/len(diagonals))

start_time = time.time()
starting_point = 7
while diagonal_members(starting_point) > 0.1:
    # print(starting_point, diagonal_members(starting_point))
    # side length has to be odd
    print("current size: ", starting_point)
    starting_point+=2
print(starting_point)

print("--- %s seconds ---" % (time.time() - start_time))