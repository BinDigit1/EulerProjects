import time
cases = 0
start = time.time()
for i in range(50):
    # 10^(n-1) < x^n <10^n
    for base in range(1,10):
        if len(str(pow(base, i))) == i:
            cases +=1
print(cases)
print("solved in ", time.time() - start,"s")