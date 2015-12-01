import time

from MathFunctions import is_pandigital

start_time = time.time()
products = set()
for i in range(1, 999):
    for j in range(9999, 11, -1):
        product = i * j
        full_num = int(str(i) + str(j) + str(product))
        if (123456789 <= full_num <= 987654321) and is_pandigital(full_num):
            # print(i, j, product)
            products.add(product)
print(sum(i for i in products))
print("--- %s seconds ---" % (time.time() - start_time))
