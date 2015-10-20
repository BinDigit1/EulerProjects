from math import pow
import time
start_time = time.time()

for i in range(2, 500):
    for j in range(i, 500):
        for k in range(j,500):
            if (i+j+k == 1000) and (pow(i,2)+pow(j,2) == pow(k,2)):
                print (i, j, k, i*j*k)

print("--- %s seconds ---" % (time.time() - start_time))