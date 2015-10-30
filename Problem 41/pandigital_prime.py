'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import MathFunctions, time

def is_pandigital(num):
    str_rep = str(num)
    string_rep_set = set(i for i in str_rep)
    if str_rep.__contains__('0'):
        return False
    length = len(str_rep)
    if length!= len(set(str_rep)):
        return False

    pan_digits = set(range(1,length+1))
    num_digits = set(ord(i) - ord('0') for i in str_rep)
    return num_digits.difference(pan_digits) == set()
start_time = time.time()
# cannot have 9 because 1+2+..+9 = 45, divisible always by 3 and 9, thus not a prime. Same for 8, sum is 36.
for i in range(7654321, 1, -2):
    if is_pandigital(i) and MathFunctions.miller_is_prime(i):
        print(i)
        break
print("--- %s seconds ---" % (time.time() - start_time))



