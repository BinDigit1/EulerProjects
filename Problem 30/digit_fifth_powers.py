
def is_digit_fifth(number):
    return sum(pow(int(i),5) for i in str(number)) == number


print(sum(fifth for fifth in range(2,9999999) if is_digit_fifth(fifth)))