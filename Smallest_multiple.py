'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
list_of_divisors = list(range(1, 21))

x=21
while(True):
    divisible_by_all = True
    #print(x)
    for number in list_of_divisors:
        if (x%number != 0):
            divisible_by_all = False
            break
    if(divisible_by_all == False):
        x+=1
    else:
        print(x)
        break

