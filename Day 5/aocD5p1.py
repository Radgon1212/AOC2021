with open('D:/Coding Playground/advent of code/Day 5 Vents/VentsMapping.txt','r') as file:
    coords = file.read().split('\n')

for n, m in enumerate(coords):
    coords[n] = m.split('->')

    for i, r in enumerate(coords[n]):
        coords[n][i] = r.split(',')

ventmap = [[0]*1000 for n in range(1000)]
count = 0

#part I
for i in range(len(coords)):
    x1 = int(coords[i][0][0])
    y1 = int(coords[i][0][1])
    x2 = int(coords[i][1][0])
    y2 = int(coords[i][1][1])
    xmin = min(x1,x2)
    xmax = max(x1,x2)
    ymin = min(y1,y2)
    ymax = max(y1,y2)

    if x1 == x2 or y1 == y2:
        for X in range(xmin , xmax+1):
            for Y in range(ymin , ymax+1):
                ventmap[X][Y] += 1
    else: 
        pass

for j in range(1000):
    for k in range(1000):
        if ventmap[j][k] > 1:
            count += 1

print('Answer for Part I:', count)

#answer for Part I is 7414
