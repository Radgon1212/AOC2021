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

'''                     
digit   no  segments
    0 = 6   a b c   e f g
    1 = 2*      c     f
    2 = 5   a   c d e f g
    3 = 5   a   c d   f g
    4 = 4*    b c d   f
    5 = 5   a b   d   f g
    6 = 6   a b   d e f g
    7 = 3*  a   c     f
    8 = 7*  a b c d e f g
    9 = 6   a b c d   f g
'''
