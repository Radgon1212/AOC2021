with open('D:/Coding Playground/advent of code/Day 7 Crab/crabs.txt','r') as file:
    position = file.read()
    position = [int(x) for x in position.split(',')]

x = 0
z = 0
d = sum(n for n in range(max(position)+1)) * len(position)

while x < max(position)+1:
    y = 0

    for i in range(len(position)):    
        for j in range(abs(position[i] - x) + 1):
            y += j
    
    if d > y:
        d = y
        z = x

    x += 1

print('Position is at', z , 'and fuel required is', d)
