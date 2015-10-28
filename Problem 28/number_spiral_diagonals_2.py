import time
def diagonal_members(size):
    diagonals = set()
    for i in range(size, 0,-2):
        # print("Layer ", i)
        for j in range(0,4):
            # print(i, j, i*i - (i-1)*j)
            diagonals.add(i*i - (i-1)*j)
    return sum(int(digit) for digit in diagonals)



start_time = time.time()
print(diagonal_members(1001))
print("--- %s seconds ---" % (time.time() - start_time))

