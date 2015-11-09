

with open("triangle.txt") as f:
    content = f.readlines()
    for x in content:
        print(x.strip("\n").split(" "))