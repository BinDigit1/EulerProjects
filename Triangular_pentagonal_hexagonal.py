import time,math

from MathFunctions import hexagonal,inverse_pentagonal, inverse_triangular


start_time = time.time()
starting_point = 144
current_hex = 0
while(True):
    current_hex=hexagonal(starting_point)
    if(not inverse_triangular(current_hex) or (not inverse_pentagonal(current_hex))):
        starting_point+=1
    else:
        break
print(current_hex)

print("--- %s seconds ---" % (time.time() - start_time))