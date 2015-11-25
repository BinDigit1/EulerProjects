from MathFunctions import is_palindrome as isp
import time
start_time = time.time()

def is_lychrel_num(num):
    current_num = num
    iteration = 0
    is_lychrel = True
    current_num = int(str(current_num)[::-1]) + current_num
    while True:
        if isp(current_num):
            is_lychrel = False
            break
        elif iteration <= 50:
            current_num = int(str(current_num)[::-1]) + current_num
            iteration += 1
        else:
            break

    return is_lychrel

print(sum(1 for i in range(0,10001) if is_lychrel_num(i)))

print("--- %s seconds ---" % (time.time() - start_time))
