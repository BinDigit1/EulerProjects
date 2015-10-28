import time, MathFunctions

start_time = time.time()


n = 1
while len(str(MathFunctions.fast_fib(n))) < 1000:
    n += 1
print(n)

print("--- %s seconds ---" % (time.time() - start_time))
