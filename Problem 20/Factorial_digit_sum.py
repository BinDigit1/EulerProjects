import time


def modified_factorial(number):
    if number==1:
        result = 1
    else:
        result = number*modified_factorial(number-1)
    return result

def int_sum(number):
    sum=0
    for i in str(int(number)):
        sum+=int(i)
    return sum


start_time = time.time()

print(int_sum(modified_factorial(100)))
print("--- %s seconds ---" % (time.time() - start_time))