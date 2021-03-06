import time, math


def count_reversibles(limit):
    counter = 0
    even_set = set(['0', '2', '4', '6', '8'])
    odd_set = set(['1', '3', '5', '7', '9'])

    for number in range(9, limit, 2):

        last_digit = number % 10
        if (last_digit == 0):
            continue
        rev_num = int(str(number)[::-1])
        sum_of_both = (number + rev_num)
        if set(str(sum_of_both)) & even_set != set():
            # print(string_repr, rev_num, sum_of_both)
            continue
        counter += 2

    return counter


start_time = time.time()

print(count_reversibles(99999999))
# print(is_reversible(619))


print("--- %s seconds ---" % (time.time() - start_time))
