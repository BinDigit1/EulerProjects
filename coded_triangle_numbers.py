'''
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import math, time


def is_triangle_num(number):
    delta = 1 + 8*number
    root = ((-1)+math.sqrt(delta))/2 #only the positive root is interesting for our case
    intRoot = int(root)

    if(intRoot==root): #checking if root is a natural number
        return True
    else:

        return False


start_time = time.time()


text_file = open("p042_words.txt", "r")
lines = text_file.read().strip('"').split('","')

number_of_triangle = 0
for word in lines:

    sum = 0
    for c in word:
        sum+=ord(c)-ord('A')+1 #calculating the "numeric" value of a character - assuming that A is 1
    if is_triangle_num(sum):
        number_of_triangle+=1
print("result: ", number_of_triangle)

print("--- %s seconds ---" % (time.time() - start_time))

