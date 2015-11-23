import time

def return_triads(perimeter):
    triads =0
    for x in range(2,perimeter):
        for y in range(x+1,perimeter-x):
            z = perimeter - x -y
            if (x*y*z)%60 ==0 and (pow(x,2) +pow(y,2) == pow(z,2)):
                triads +=1

    return triads

start_time = time.time()
# print(return_triads(120))
max_triads, max_triads_index = 0,0
for i in range(1,1001):

    current_count = return_triads(i)
    if current_count > max_triads:

        max_triads = current_count
        max_triads_index = i
        print(i, max_triads)
print("max: ", max_triads_index)

print("--- %s seconds ---" % (time.time() - start_time))
