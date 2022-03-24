file = open('D:/Coding Playground/advent of code/Day 1 Sonar/inputd1sonar.txt','r')
lines = file.readlines()
increased = 0
decreased = 0

for i in range(len(lines)-3):
    if int(lines[i]) < int(lines[i+3]):
        increased += 1

    elif int(lines[i]) > int(lines[i+3]):
        decreased += 1

    else:
        pass 

print(increased)
