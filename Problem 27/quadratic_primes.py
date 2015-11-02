import MathFunctions

def function_generator(a, b):
    def f(h):
        return h*h + a*h + b
    return f

def function_tester(f):
    count = 0
    for n in range(0,100):
        if not MathFunctions.miller_is_prime(abs(f(n))):
            break
        count+=1
    return count

current_max, product = 0 , 0
for a in range(-1000,1000):
    for b in range(-1000, 1000):
        current_function = function_generator(a,b)
        number_of_primes_now = function_tester(current_function)
        if function_tester(current_function)>current_max:
            current_max = number_of_primes_now
            print("current max combo: ", a, b, current_max)
            product = a*b
print(product)






