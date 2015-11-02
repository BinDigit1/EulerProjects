import MathFunctions

def function_generator(a, b):
    def f(h):
        return h*h + a*h + b
    return f

def function_tester(f):
    count = 0
    for n in range(0,100):
        if not MathFunctions.miller_is_prime(f(n)):
            break
        count+=1
    return count


for a in range(-1000,1000):
    for b in range(-1000, 1000):
        current_function = function_generator(a,b)



