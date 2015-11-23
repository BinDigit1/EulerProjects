def return_triads(perimeter):
    triads =set()
    for x in range(3,perimeter):
        for y in range(2,perimeter):
            for z in range(5,perimeter):
                if x+y+z==perimeter and pow(x,2) + pow(y,2) == pow(z,2):

                    print(x, y, z)
                    triads.add({x,y,z})
    return triads

print(return_triads(120))
