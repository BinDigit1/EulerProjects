import math


s = lambda x: sum(int(i) for i in str(x))

# for i in range(10, 9999999):
#     for exp in range(1, 8):
#
#         if pow(s(i),exp) == i:
#             print(i,s(i),exp)
index =1
for i in range(11,100000000000000):


    if s(i)>6:

        if math.pow(s(i),round(math.log(i,s(i)))) == i:

            print(index,': ',i,s(i))
            index += 1
