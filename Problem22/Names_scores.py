
fo = open("p022_names.txt",'r')
names =fo.read().strip('"').split('","').sort()

print(names)