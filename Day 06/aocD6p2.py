with open('D:/Coding Playground/advent of code/Day 6 Lanternfish/Lanternfish.txt','r') as file:
    lantern = file.read().split(',')
    lantern = [int(x) for x in lantern]

timer = [0]*9

for i in range(9):
    for x in range(len(lantern)):
        if i == lantern[x]:
            timer[i] += 1

days = 256
temp = 0

for j in range(days):
    temp = timer[0]
    
    for k in range(len(timer)-1):
        timer[k] = timer[k+1]
    
    timer[6] += temp
    timer[8] = temp

print('Answer for part II:', sum(timer))
