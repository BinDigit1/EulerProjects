'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ? 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def isPalindrome(number):
    string_rep = str(number)
    inversed = string_rep[::-1]

    if (inversed == string_rep):
        return True
    return False


largest_parts = []
largest =0
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if (isPalindrome(product)):
            if largest < product:
                largest = product
                if(len(largest_parts)>0):
                    largest_parts.pop()
                    largest_parts.pop()
                largest_parts.append(i)
                largest_parts.append(j)
print(largest_parts)
print(largest)
