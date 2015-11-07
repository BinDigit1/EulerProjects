import tree, pprint

with open("triangle.txt") as f:
    content = f.readlines()
    dic = {}
    level = 0
    for x in content:
        dic[level] =x.strip("\n").split(" ")
        level += 1
    pprint.pprint(dic)