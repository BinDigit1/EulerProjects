# test_num = 1406357289
import time

def is_pandigital(num):
    set_of_num = set(i for i in str(num))
    set_of_all_digits = set(str(i) for i in range(0, 10))
    return len(str(num)) == len(set_of_num) and set_of_all_digits.difference(set_of_num) == set()

start_time = time.time()
multiples_of_17 =[str(i*17).zfill(3) for i in range(1,59) if i*17<999]

multiples_of_13 =[str(i*13).zfill(3) for i in range(1,77) if i*13<999]
multiples_of_11 =[str(i*11).zfill(3) for i in range(10,91) if i*11<999 and (str(i*11).zfill(3)[0] =='0' or str(i*11).zfill(3)[0] =='5')]
multiples_of_7 =[str(i*7).zfill(3) for i in range(1,143) if i*7<999]


last_part = []

for i in multiples_of_17:
    for j in multiples_of_13:
        for k in multiples_of_11:
            for l in multiples_of_7:
                # print(l, k, j, i)
                if i[0:2] == j[1:] and k[1:] == j[0:2] and l[1:3]==k[0:2]:
                    last_part.append(l+k[2]+i[1:])

sum_all = 0
for i in range(1000, 10000,2): #fourth digit must be even
    for j in last_part:
        current = (str(i)+j)
        if is_pandigital(int(current)) and int(current[2:5])%3==0: #here we consider the last constraint: the divisibility by 3
            sum_all += int(current)
print(sum_all)
print("--- %s seconds ---" % (time.time() - start_time))
