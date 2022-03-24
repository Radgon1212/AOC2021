import numpy as np
from scipy.signal import argrelextrema

with open('D:/Coding Playground/advent of code/Day 9 Heightmap/Heightmap.txt','r') as file:
    heightmap = file.read().split('\n')

row = len(heightmap)

for i in range(row):
    heightmap[i] = list(int(x) for x in heightmap[i])

col = len(heightmap[0])

rotatemap = [[0] * row for c in range(col)]
lowpoints = [0] * row
lowrotate = [0] * col
sum = 0

for j in range(row):
    for k in range(col):
        rotatemap[k][j] = heightmap[j][k] 

#arranging map & checking local minimas, missing out first and last element

for l in range(row):
    heightmap[l] = np.array(heightmap[l])
    lowpoints[l] = argrelextrema(heightmap[l], np.less)
#missed out minimas for 0th col and -1th col

for m in range(col):
    rotatemap[m] = np.array(rotatemap[m])
    lowrotate[m] = argrelextrema(rotatemap[m], np.less)
#missed out minimas for 0th row and -1th row

#matching horizontal minimas with vertical minimas for 2d minima
x = 0
for o in range(1,row-1):

    for p in range(len(lowpoints[o][0])):
        x = lowpoints[o][0][p]
        
        if (o in lowrotate[x][0]):
            sum += heightmap[o][x]
            sum += 1
        
        else:
            pass

# checking for 0th row/col and -1th row/col
q = 0
while q > -2:
    
    for p in range(len(lowpoints[q][0])):
        x = lowpoints[q][0][p]
        if heightmap[q][x] < heightmap[3*q+1][x]:
            sum += heightmap[q][x]
            sum += 1

    for p in range(len(lowrotate[q][0])):
        x = lowrotate[q][0][p]
        if rotatemap[q][x] < rotatemap[3*q+1][x]:
            sum += rotatemap[q][x]
            sum += 1

    if heightmap[q][q] < heightmap[q][3*q+1]:
        if heightmap[q][q] < heightmap[3*q+1][q]:
            sum += heightmap[q][q]
            sum += 1
        
        else: pass
    else: pass

    q -= 1

print(sum)
'''
missed out by lowpoints
v       v
x x x x x < missed out by lowrotate
x x x x x
x x x x x
x x x x x < missed out by lowrotate

'''
