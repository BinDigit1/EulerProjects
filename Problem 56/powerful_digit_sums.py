import time

start = time.time()
largest = 0
for i in range(1,100):
    for j in range(100,1,-1):
        c = sum(int(i) for i in str(pow(i,j)))
        if c>largest:
            largest = c
print(largest)
print("solved in ", time.time() - start,"s")