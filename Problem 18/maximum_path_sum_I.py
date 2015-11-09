
with open("small_triangle.txt") as f:
    content = f.readlines()
    list_normal, reversed_list = list(), list()
    for x in content:
        list_normal.append((x.strip("\n").split(" ")))
    for x in reversed(content):
        reversed_list.append((x.strip("\n").split(" ")))

def take_first_column(list_a, after_row=0):
    temp = [row[0] for row in list_a]
    return temp[after_row:]
def sum_of_items(list_a):
    return sum(int(i) for i in list_a)

print(list_normal)
print(take_first_column(list_normal,1))
print(sum_of_items(take_first_column(list_normal)))
