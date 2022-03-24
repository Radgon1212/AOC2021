with open('D:/Coding Playground/advent of code/Day 10 Chunks/Chunks.txt','r') as file:
    chunks = file.read().split('\n')

def check(expression):

    open_bracket = tuple('({[<')
    close_bracket = tuple(')}]>')
    map = dict(zip(open_bracket, close_bracket))
    queue = []
    score = 0
    scorelist = []

    for element in expression:
        queue.clear()

        for bracket in element:

            if bracket in open_bracket:
                queue.append(map[bracket])
            
            elif bracket in close_bracket:
                if len(queue) == 0 or bracket != queue.pop():
                    queue.clear()
                    break

                else:
                    pass

        while len(queue) > 0:
            required = queue.pop()
            score *= 5

            if required == ')':
                score += 1

            elif required == ']':
                score += 2

            elif required == '}':
                score += 3

            elif required == '>':
                score += 4

        if score > 0:
            scorelist.append(score)
            score = 0

    scorelist = sorted(scorelist)
    middex = int((len(scorelist)) / 2)
    return(scorelist[middex])

print(check(chunks))