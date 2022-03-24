with open('D:/Coding Playground/advent of code/Day 4 Bingo/BingoBoard.txt','r') as file:
    bingo = file.read().split("\n\n")

for n, m in enumerate(bingo):
    bingo[n] = m.split("\n")
    
    for i, r in enumerate(bingo[n]):
        bingo[n][i] = r.split()

with open('D:/Coding Playground/advent of code/Day 4 Bingo/BingoNumbers.txt','r') as file2:
    numberlist = file2.read().split(",")

fastest = len(numberlist)
board = 0
last = 0
y = 0
x = 0
    
for i in range(len(bingo)): 
#range of i is 0 - 99, number of bingo board
    row = [0, 0, 0, 0, 0]
    col = [0, 0, 0, 0, 0]

    for j in range(fastest):
        called = numberlist[j]
    
        if any(q == 5 for q in row) or any(q == 5 for q in col):
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
                    bingo[i][x][y] ='X'

            if row[x] == 5 or col[y] == 5:
                fastest = j
                board = i
                total = 0
                last = int(called)
                
                for k in range(5):
                    for element in bingo[board][k]:
                        if isinstance(element, int) or element.isdigit():
                            total += int(element)
                            
winner = total * last
print('First to bingo in', fastest+1, 'moves')  
print('Board number is', board+1)                  
print('Sum of unmarked numbers =', total)
print('Last called number =', last)
print('Answer for Part I is ', winner)

#answer is 89001