import MathFunctions
def isDigitFactorial(number):
    sum = 0
    for i in str(number):
        sum += MathFunctions.factorial(int(i))
    # print(number, sum)
    return sum == number


sum = 0
for i in range(3, 10000000):

    if(isDigitFactorial(i)):
        sum += i

print(sum)