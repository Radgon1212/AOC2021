with open('D:/Coding Playground/advent of code/Day 8 Display/segment.txt','r') as file:
    segment = file.read().split('\n')
for n,m in enumerate(segment):
    segment[n] = m.split(' | ')
    for o,p in enumerate(segment[n]):
        segment[n][o] = p.split(' ')

total = 0
output = ['']*len(segment)

for i in range(len(segment)):
    digit = ['']*10
    wire = ['']*7
    temp = sorted(segment[i][0], key=len)

    digit[1] = set(temp[0])
    digit[7] = set(temp[1])
    digit[4] = set(temp[2])
    digit[8] = set(temp[9])

    wire[0] = digit[7] - digit[1]     
        
    for j in range(3,6):
        if len(set(temp[j]) - digit[7]) == 2:
            digit[3] = set(temp[j])

    for k in range(6,9):
        if len(set(temp[k]) - digit[3]) == 1:
            digit[9] = set(temp[k])
    
    wire[1] = digit[9] - digit[3]

    for m in range(3,6):
        if len(set(temp[m]) - wire[1]) == 4:
            digit[5] = set(temp[m])

    for n in range(6,9):
        if len(digit[7] - set(temp[n])) == 1:
            digit[6] = set(temp[n])
        
    wire[4] = digit[6] - digit[5]
    wire[2] = digit[8] - digit[6]
    wire[6] = digit[9] - wire[0] - digit[4]
    wire[3] = digit[3] - digit[7] - wire[6]
    digit[2] = set.union(wire[0], wire[2], wire[3], wire[4], wire[6])
    digit[0] = digit[8] - wire[3]
    wire[5] = digit[7] - digit[2]

    for o in range(len(segment[i][1])):
        for p in range(10):
            if set(segment[i][1][o]) == digit[p]:
                segment[i][1][o] = str(p)
    
    output[i] = segment[i][1][0] + segment[i][1][1] + segment[i][1][2] + segment[i][1][3]
    
total = sum(int(element) for element in output)

print(total)
