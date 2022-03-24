with open('D:/Coding Playground/advent of code/Day 8 Display/segment.txt','r') as file:
    segment = file.read().split('\n')
for n,m in enumerate(segment):
    segment[n] = m.split(' | ')
    for o,p in enumerate(segment[n]):
        segment[n][o] = p.split(' ')

count = 0

for i in range(len(segment)):
    for j in range(len(segment[i][1])):
        a = len(segment[i][1][j])
        if a <= 4 or a == 7:
            count += 1

print(count)
