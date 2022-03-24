with open('D:/Coding Playground/advent of code/Day 11 Dumbo Octopus/Octopus.txt','r') as file:
    octopus = file.read().split('\n')

for i in range(len(octopus)):
    octopus[i] = list(int(j) for j in octopus[i])

def outbreak(location,x0,y0):
    adj_cell = [-1, 0, 1]

    for m in adj_cell:
        for n in adj_cell:
            
            if m == 0 and n == 0:
                pass

            else:
                x2 = x0 + m
                y2 = y0 + n

                if x2 < 0 or y2 < 0 or x2 >= len(location) or y2 >= len(location[x0]):
                    pass

                elif location[x2][y2] == 'X':
                    pass
                
                elif location[x2][y2] <= 9:
                    location[x2][y2] += 1
                    
                    if location[x2][y2] == 10:
                        location[x2][y2] = 'X'
                        outbreak(location,x2,y2)
                
    return

def flashes(start):
    x = 0
    z = 0
    r = len(start)

    while z < 100:
        z = 0
        
        for i in range(r):
            for j in range(len(start[i])):
                if start[i][j] == 'X':
                    pass
                else:
                    start[i][j] += 1

                if start[i][j] == 10:
                    start[i][j] = 'X'
                    outbreak(start,i,j)
        
        for i in range(r):
            for j in range(len(start[i])):
                    if start[i][j] == 'X':
                        z += 1
                        start[i][j] = 0

        x += 1

    return(x)

print(flashes(octopus))
