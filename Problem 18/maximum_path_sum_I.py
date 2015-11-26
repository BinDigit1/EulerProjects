import time
file_stream = open('triangle.txt')

num_lines = 0
with file_stream as f:
    content = f.readlines()
    list_normal, reversed_list = list(), list()
    for x in content:
        list_normal.append((x.strip("\n").split(" ")))
        num_lines += 1
    for x in content:
        inv = (x.strip("\n").split(" "))
        inv.reverse()
        reversed_list.append(inv)

def take_nth_column(list_a, n=0, after_row=0):
    temp = [row[n] for row in list_a[after_row:]]#[after_row:]
    return temp
def sum_of_items(list_a):
    return sum(int(i) for i in list_a)

start_time =time.time()
level = 1
left_index, right_index = 0, 0
max_sum = int(list_normal[0][0])
# print(max_sum)
for i in range(1, num_lines):
    level = i
    if sum_of_items(take_nth_column(list_normal,left_index, level)) >  sum_of_items(take_nth_column(reversed_list,right_index, level)):
        print(sum_of_items(take_nth_column(list_normal,left_index, level)), '...', sum_of_items(take_nth_column(reversed_list,right_index, level)))
        print(take_nth_column(list_normal,left_index, level), ' > ', take_nth_column(reversed_list,right_index, level), ' L')
        max_sum += int(take_nth_column(list_normal,left_index, level)[0])

        right_index += 1
    else:
       max_sum += int(take_nth_column(reversed_list,right_index, level)[0])
       print(take_nth_column(list_normal,left_index, level), ' < ', take_nth_column(reversed_list,right_index, level), ' R')

       left_index += 1


print(max_sum)
print("--- %s seconds ---" % (time.time() - start_time))