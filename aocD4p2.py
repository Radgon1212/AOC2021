with open('D:/Coding Playground/advent of code/Day 4 Bingo/BingoBoard.txt','r') as file:
    bingo = file.read().split("\n\n")

for n, m in enumerate(bingo):
    bingo[n] = m.split("\n")
    
    for i, r in enumerate(bingo[n]):
        bingo[n][i] = r.split()

with open('D:/Coding Playground/advent of code/Day 4 Bingo/BingoNumbers.txt','r') as file2:
    numberlist = file2.read().split(",")

slowest = 0
board = 0
last = 0
x = 0
y = 0
    
for i in range(len(bingo)): 
#range of i is 0 - 99, number of bingo board
    row = [0, 0, 0, 0, 0]
    col = [0, 0, 0, 0, 0]

    for j in range(len(numberlist)):
        called = numberlist[j]
    
        if any(x == 5 for x in row) or any(y == 5 for y in col):
            break
        
        else:
            for X in range(5):
            #number of columns of each bingo board        

                try:
                    bingo[i][X].index(called)

                except ValueError:
                    pass

                else:
                    x = X
                    y = bingo[i][x].index(called)
                    row[x] += 1
                    col[y] += 1
                    bingo[i][x][y] = 'X'

            if (row[x] == 5 or col[y] == 5):
                if j < slowest:
                    break
                
                else:
                    slowest = j
                    board = i
                    last = int(called)
                    total = 0

                    for k in range(5):
                        for element in bingo[i][k]:
                            if isinstance(element, int) or element.isdigit():
                                total += int(element)
    
loser = total * last
print('Last to bingo in', slowest+1, 'moves')  
print('Board number is', board+1)                  
print('Sum of unmarked numbers =', total)
print('Last called number =', last)
print('Answer for Part II is ', loser)

#answer is 7296