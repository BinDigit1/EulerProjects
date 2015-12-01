
import time
def self_power_series(i):
    sum = 0
    for i in range(1,i+1):
        sum+=pow(i,i)
    return sum

start_time = time.time()
print(str(self_power_series(1000))[-10:])

print("--- %s seconds ---" % (time.time() - start_time))
