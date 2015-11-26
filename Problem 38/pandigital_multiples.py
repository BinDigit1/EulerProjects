import MathFunctions, time


start_time = time.time()
found, i = '', 9999
while found =='':

    concatenated =''
    for n in range(1,5):
        current  = i*n
        concatenated += str(current)
        if int(concatenated)<123456789:
            continue
        elif int(concatenated)>987654321:
            break
        elif MathFunctions.is_pandigital(int(concatenated)):
            found = concatenated
    i -= 1
print(found)
print("--- %s seconds ---" % (time.time() - start_time))
