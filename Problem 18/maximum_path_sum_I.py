file_stream = open('small_triangle.txt')

num_lines = 0
with file_stream as f:
    content = f.readlines()
    list_normal, reversed_list = list(), list()
    for x in content:
        list_normal.append((x.strip("\n").split(" ")))
        num_lines += 1
    for x in reversed(content):
        reversed_list.append((x.strip("\n").split(" ")))

def take_nth_column(list_a, n=0, after_row=0):
    temp = [row[n] for row in list_a][after_row:]
    return temp
def sum_of_items(list_a):
    return sum(int(i) for i in list_a)

level = 1

print(num_lines)
print(take_nth_column(list_normal,0, level))
print(sum_of_items(take_nth_column(list_normal,0,level)))
