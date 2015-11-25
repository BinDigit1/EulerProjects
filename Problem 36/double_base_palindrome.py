import MathFunctions, time
start_time = time.time()
print(sum(i for i in range(1,1000000) if MathFunctions.is_palindrome(i) and MathFunctions.is_palindrome ("{0:b}".format(i))))
print("--- %s seconds ---" % (time.time() - start_time))