import time
fo = open("p022_names.txt",'r')
names =sorted(fo.read().strip('"').split('","'))

'''
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
'''
def score(word):
    sum = 0
    for i in word:

        sum += ord(i)-ord('A')+1
    return sum


start_time = time.time()
sumOfNames, cursor = 0, 1
for i in names:
    sumOfNames += score(i) * cursor
    cursor+=1
print(sumOfNames)
# print(score('COLIN'))
print("--- %s seconds ---" % (time.time() - start_time))