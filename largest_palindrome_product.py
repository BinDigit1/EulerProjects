'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ? 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

def is_palindrome(number):
    string_rep = str(number)
    inverse = string_rep[::-1]

    if inverse == string_rep:
        return True
    return False

start_time = time.time()
largest_parts = []
largest =0
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if (is_palindrome(product)):
            if largest < product:
                largest = product
                if(len(largest_parts)>0):
                    largest_parts.pop()
                    largest_parts.pop()
                largest_parts.append(i)
                largest_parts.append(j)
print(largest_parts)
print(largest)
print("--- %s seconds ---" % (time.time() - start_time))
