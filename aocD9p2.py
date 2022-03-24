with open('D:/Coding Playground/advent of code/Day 9 Heightmap/Heightmap.txt','r') as file:
    heightmap = file.read().split('\n')
    
row = len(heightmap)
col = len(heightmap[0])
connectedsets = [list() for n in range(row)]
temp = set()

for i in range(row):
    heightmap[i] = list(int(x) for x in heightmap[i])
    started = False
    k = 0

    for j in range(len(heightmap[i])):
        y = heightmap[i][j]

        if y == 9:
            heightmap[i][j] = 'X'

            if started == False:
                pass

            else:
                started = False
                connectedsets[i].append(set(temp))
                temp.clear()
                k += 1

        else: 
            heightmap[i][j] = 1
            temp.add(j)

            if j == (col-1):
                started = False
                connectedsets[i].append(set(temp))
                temp.clear()

            elif started == False:
                started = True

            else:
                pass

count = 0
basinsize = [0,0,0]
updown = [-1, 1]
checking = [list() for n in range(row)]
element = set()
y = 0
x = 0
mindex = 0

for r in range(row):
    temp.clear()

    while len(connectedsets[r]) > 0:
        temp = connectedsets[r].pop(0)
        checking[r].append(temp)
        z = 0

        while any(checking):
            x = r

            while x <= row:
                if len(checking[x]) > 0:
                    break
                else: x += 1

            if x > row:
                break
            else: 
                element = checking[x].pop(0)
            
            z += len(element)

            for i in range(2):
                y = x + updown[i]

                if y < r or y >= row:
                    pass

                elif len(connectedsets[y]) == 0:
                    pass
                
                else:
                    for s in connectedsets[y]:

                        if min(s) > max(element):
                            break

                        elif len(element & s) > 0:
                            checking[y].append(s)
                
                    for s in checking[y]:
                        try:
                            connectedsets[y].remove(s)
                        except:
                            pass
            
        if z > min(basinsize):
            mindex = basinsize.index(min(basinsize))
            basinsize[mindex] = z

print(basinsize)

part2 = 1

for z in basinsize:
    part2 *= z

print(part2)