
import time
def is_reversible(number):
    string_repr = str(number)


    if (string_repr[-1] =='0'):
        return False

    sum_of_digits = 0
    for i in string_repr:
        sum_of_digits += (ord(i) - ord('0'))
    print(sum_of_digits)
    #
    # if (sum_of_digits%2) == 0:
    #     return False


    sum_of_both = (number+int(string_repr[::-1]))
    for i in str(sum_of_both):
        # print(i)
        if int(i)%2 ==0 :
            return False
    # print(number, int(string_repr[::-1]), sum_of_both)
    return True

start_time = time.time()

print(sum(1 for i in range(1,1000) if is_reversible(i)))
# print(is_reversible(619))
print("--- %s seconds ---" % (time.time() - start_time))