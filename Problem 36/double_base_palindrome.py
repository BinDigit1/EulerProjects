# print("{0:b}".format(12))

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

print(sum(i for i in range(1,1000000) if is_palindrome(i) and is_palindrome("{0:b}".format(i))))