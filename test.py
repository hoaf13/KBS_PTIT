f = open('test.txt', 'r')
index1 = 0
index2 = 5
for index,line in enumerate(f):
    if index == index1:
        index1 += 6
        print(line[:-1], end = " ")
    if index == index2:
        index2 += 6
        print(line[:-1])