file = open("D:/Coding Playground/advent of code/Day 2 Submarine/inputd2sub.txt", "r")
lines = file.read().split('\n')
x = 0
y = 0

#answer for part I is 2027977
#answer for part II is 1903644897


for i in range(len(lines)):
    s = str.strip(lines[i])

    if s[0] == 'f':
        x += int(s[-1])
       
    elif s[0] == 'd':
        y += int(s[-1])

    elif s[0] == 'u':
        y -= int(s[-1])

print (x)
print (y)
print ('Answer for Part I : ', x*y)

horizontal = 0
aim = 0
depth = 0
dive = 0

for i in range(len(lines)):
    s = str.strip(lines[i])

    if s[0] == 'f':
        horizontal += int(s[-1])
        dive = aim*int(s[-1])
        depth += dive

    elif s[0] == 'd':
        aim += int(s[-1])

    elif s[0] == 'u':
        aim -= int(s[-1])

print('Answer for Part II is : ', horizontal*depth)
