'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import MathFunctions, itertools
def is_permuted(a, b):
    list_of_permutations =[int(''.join(x)) for x in itertools.permutations(str(a))]
    return list_of_permutations.__contains__(b)
for i in range(1489, 10000):
    if MathFunctions.miller_is_prime(i) and MathFunctions.miller_is_prime(i+3330) and MathFunctions.miller_is_prime(i+6660)\
            and is_permuted(i,i+3330) and is_permuted(i, i+6660):
        print(i, i+3330, i+6660)
        break
