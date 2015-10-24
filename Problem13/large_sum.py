
import time
start_time = time.time()
lines = [int(line.rstrip('\n')) for line in open('nums.txt')]
sum = 0
for i in lines:
    sum += i

print(str(sum)[:10])
print("--- %s seconds ---" % (time.time() - start_time))
