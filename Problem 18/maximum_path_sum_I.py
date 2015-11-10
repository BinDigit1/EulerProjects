file_stream = open('small_triangle.txt')

num_lines = 0
with file_stream as f:
    content = f.readlines()
    list_normal, reversed_list = list(), list()
    for x in content:
        list_normal.append((x.strip("\n").split(" ")))
        num_lines += 1
    for x in content:
        list_normal.append((x.strip("\n").split(" ")))

def take_nth_column(list_a, n=0, after_row=0):
    temp = [row[n] for row in list_a][after_row:]
    return temp
def sum_of_items(list_a):
    return sum(int(i) for i in list_a)

level = 1
left_index, right_index = 0, 0
print( reversed_list)
# for i in range(1, num_lines):
#     level = i
#     if sum_of_items(take_nth_column(list_normal,left_index, level)) >  sum_of_items(take_nth_column(reversed_list,right_index, level)):
#         print(take_nth_column(list_normal,left_index, level)[0])
#         right_index += 1
#     else:
#         print(take_nth_column(reversed_list,right_index, level)[0])
#         left_index += 1

