with open('D:/Coding Playground/advent of code/Day 10 Chunks/Chunks.txt','r') as file:
    chunks = file.read().split('\n')

def check(expression):

    open_bracket = tuple('({[<')
    close_bracket = tuple(')}]>')
    map = dict(zip(open_bracket, close_bracket))
    queue = []

    score = [0,0,0,0]

    for element in expression:
        queue.clear()

        for bracket in element:

            if bracket in open_bracket:
                queue.append(map[bracket])
            
            elif bracket in close_bracket:
                if len(queue) == 0 or bracket != queue.pop():
                    if bracket == ')':
                        score[0] += 3
                    
                    elif bracket == ']':
                        score[1] += 57

                    elif bracket == '}':
                        score[2] += 1197

                    elif bracket == '>':
                        score[3] += 25137

                    break

                else:
                    pass

    return(score,sum(score))

print(check(chunks))