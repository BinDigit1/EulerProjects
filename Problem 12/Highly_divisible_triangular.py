
import time, math


def getMyDivisors(num):
    total = 0
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            total += 2
    # print(num, total) #the number itself is also a divisor

    return total
all_naturals ={1:1}
def natural(n):
    if not n in all_naturals:
        all_naturals[n]= n +natural(n-1)
    return all_naturals[n]



start_time = time.time()
n = 2
while True:

    current = natural(n)
    if current%2 ==1:
        n+=1
    elif getMyDivisors(current)>500:
        print(current)
        break
    else:
        n+=1
print("--- %s seconds ---" % (time.time() - start_time))

