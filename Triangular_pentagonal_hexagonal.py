import time,math

def triangular(number):
    return number*(number+1)/2

def inverse_triangular(number):
    delta = 1+8*number
    root = (-1 + math.sqrt(delta))/2

    return root==int(root)

def pentagonal(number):
    return number*(3*number-1)/2

def inverse_pentagonal(number):
    delta = 1+24*number
    root = (1 + math.sqrt(delta))/6

    return root==int(root)

def hexagonal(number):
    return number*(2*number - 1)

def inverse_hexagonal(number):
    delta = 1+8*number
    root = (1 + math.sqrt(delta))/4

    return root==int(root)


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