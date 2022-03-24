from collections import Counter
with open('D:/Coding Playground/advent of code/Day 3 Binary/inputD3.txt','r') as file:
    lines = file.readlines()

gamma = []
epsilon = []

for i in range(12):
    count1 = 0
    count0 = 0

    for j in range(len(lines)):
        report = lines[j]
      
        if report[i] == '1':
            count1 += 1

        else:
            count0 += 1
    
    if count1 > count0:
        gamma.append(1)
        epsilon.append(0)

    elif count0 > count1:
        gamma.append(0)
        epsilon.append(1)

gammadeci = int("".join(str(x) for x in gamma), 2)
epsilondeci = int("".join(str(x) for x in epsilon), 2)

print('Gamma Binary is ', str(gamma))
print('Epsilon Binary is ', str(epsilon))

print('Gamma is : ', gammadeci)
print('Epsilon is : ', epsilondeci)

print('Answer for Part I : ', gammadeci*epsilondeci)
#part I is 2498354


O2 = lines
CO2 = lines


for i in range(12):
    count0 = 0
    count1 = 0
    list0 = []
    list1 = []

    for j in range(len(O2)):
        report = O2[j]

        if report[i] == '1':
            count1 += 1
            list1.append(report)

        elif report[i] == '0':
            count0 += 1
            list0.append(report)

    if count0 > count1:
        O2 = list0

    else:
        O2 = list1

print('Oxygen amount : ', str(O2))

for i in range(12):
    count0 = 0
    count1 = 0
    list0 = []
    list1 = []
    if len(CO2) == 1:
        break

    for j in range(len(CO2)):
        report = CO2[j]

        if report[i] == '1':
            count1 += 1
            list1.append(report)

        elif report[i] == '0':
            count0 += 1
            list0.append(report)

    if count1 < count0:
        CO2 = list1

    else:
        CO2 = list0

print('Oxygen amount : ', str(CO2))

O2deci = int("".join(str(x) for x in O2), 2)
CO2deci = int("".join(str(x) for x in CO2), 2)

print('Answer for Part II : ', O2deci*CO2deci)
#part II is 3277956
