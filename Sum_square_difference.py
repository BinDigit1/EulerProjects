'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 ? 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
from math import  pow
first_one_hundrend=list(range(1,101))
first_one_hundrend_sum =list()
sum_first_one_hundrend = 0
for number in first_one_hundrend:
    sum_first_one_hundrend += number
    first_one_hundrend_sum.append(pow(number,2))
sum_first_one_hundrend = pow(sum_first_one_hundrend, 2)
print(sum_first_one_hundrend)
sum_of_squares = 0
for number in first_one_hundrend_sum:
    sum_of_squares+=number
print(sum_first_one_hundrend - sum_of_squares)