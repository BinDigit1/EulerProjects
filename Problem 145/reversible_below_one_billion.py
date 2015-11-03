
import time
def count_reversibles(limit):
    counter = 0
    reversible_list, non_reversible_list = set(), set()
    for number in range(1, limit):
        string_repr = str(number)
        if number in reversible_list or number in non_reversible_list:
            # print("found existing instance: ", number)
            continue



        if (number%10 == 0):
            continue
        rev_num = int(string_repr[::-1])
        #
        # if (sum_of_digits%2) == 0:
        #     return False

        sum_of_both = (number+rev_num)
        # print(number,int(string_repr[::-1]), sum_of_both )
        is_reversible = True
        for i in str(sum_of_both):
            # print(i)
            if int(i)%2 ==0 :
                is_reversible = False
                break
        if is_reversible:
            reversible_list.add(number)
            reversible_list.add(rev_num)
            print(number, sum_of_both)

        else:
            non_reversible_list.add(number)
            non_reversible_list.add(rev_num)
    return len(reversible_list)

start_time = time.time()

print(count_reversibles(10000))
# print(is_reversible(619))
print("--- %s seconds ---" % (time.time() - start_time))