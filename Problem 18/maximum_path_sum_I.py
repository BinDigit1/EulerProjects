pos_y, pos_x, lines = 0, 0, 0

class Node:
    def __init__(self, x,y,value):
        self.x = x
        self.y = y
        self.value = value
    def __str__(self):
        return str(self.x)+','+str(self.y)+': '+str(self.value)



list_of_nodes, list_of_reversed_nodes = list(), list()
for line in (open("triangle.txt").readlines()):
    pos_y += 1
    lines += 1
    pos_x = 0
    for x in line.rstrip().split(" "):
        pos_x +=1
        list_of_nodes.append(Node(pos_x,pos_y,x))
    for x in reversed(line.rstrip().split(" ")):
        pos_x +=1
        list_of_reversed_nodes.append(Node(pos_x,pos_y,x))
st = ''
print("total lines: ", lines)
for item in filter(lambda item: item.x == 1 and item.y<15, list_of_nodes):

    st = st + " "+ item.value
print(st)