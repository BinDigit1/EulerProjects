import time
output = ''
i=1
start_time = time.time()
while len(output)<1000001:

    output +=str(i)
    i += 1

print(int(output[9]) * int(output[99]) *
      int(output[999]) * int(output[9999]) *
      int(output[99999]) * int(output[999999]))

print("--- %s seconds ---" % (time.time() - start_time))