with open('D:/Coding Playground/advent of code/Day 13 Origami/Dots.txt','r') as file:
    manual = file.read().split('\n\n')

dots = manual[0].split('\n')
folding = manual[1].split('\n')

for i, m in enumerate(dots):
    dots[i] =  m.split(',')

    for j in range(2):
        dots[i][j] = int(dots[i][j])

for k, n in enumerate(folding):
    folding[k] = n.split('=') 

def origami(pattern,instruction,step):
    count = 0

    for i in range(step):
        line = int(instruction[i][1])

        if instruction[i][0][-1] == 'x':
            foldalongX(pattern, line)

        else:
            foldalongY(pattern, line)

        pattern.sort()
        overlap(pattern)

    count = len(pattern)
    return(count)

def foldalongX(pattern, line):

    for i in range(len(pattern)):
        if pattern[i][0] > line:
            pattern[i][0] = 2 * line - pattern[i][0]

def foldalongY(pattern, line):

    for i in range(len(pattern)):
        if pattern[i][1] > line:
            pattern[i][1] = 2 * line - pattern[i][1]

def overlap(pattern):
    temp = list()

    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            temp.append(i+1)

    while len(temp) > 0:
        pattern.pop(temp.pop())

print(origami(dots,folding,1))