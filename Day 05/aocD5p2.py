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
    
    elif x1 == xmin and y2 == ymin:
        Y = y1
        
        for X in range(x1,x2+1):
            ventmap[X][Y] += 1
            Y -= 1
    
    elif x2 == xmin and y1 == ymin:
        Y = y1

        for X in range(x1,x2-1,-1):
            ventmap[X][Y] += 1
            Y += 1
    
    else:
        Y = ymin
        for X in range (xmin,xmax+1):
            ventmap[X][Y] += 1
            Y += 1

for j in range(1000):
    for k in range(1000):
        if ventmap[j][k] > 1:
            count += 1

print('Answer for part II:', count)

#answer for Part II is 19676
