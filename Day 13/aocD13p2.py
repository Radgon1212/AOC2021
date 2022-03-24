from email import message
from subprocess import call
import numpy as np

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

def origami(pattern,instruction):
    message = list()

    for i in range(len(instruction)):
        line = int(instruction[i][1])

        if instruction[i][0][-1] == 'x':
            foldalongX(pattern, line)

        else:
            foldalongY(pattern, line)

        pattern.sort()
        overlap(pattern)

    message = readpattern(pattern)
    
    return(message)

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

#print(origami(dots,folding))

def readpattern(pattern):

    allX = list()
    allY = list()

    for i in range(len(pattern)):
        allX.append(pattern[i][0])
        allY.append(pattern[i][1])

    maxX = max(allX)
    maxY = max(allY)

    message = [[' ']*(maxX+1) for n in range(maxY+1)]

    for i in range(len(pattern)):
        x = pattern[i][0]
        y = pattern[i][1]
        message[y][x] = '*'

    message = np.array(message)

    return(message)

for line in origami(dots,folding):
    print(''.join(map(str,line)))
