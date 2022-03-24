with open('D:/Coding Playground/advent of code/Day 12 Routes/Caves.txt','r') as file:
    cavespair = file.read().split('\n')

cavesname = set()

for n,m in enumerate(cavespair):
    cavespair[n] = m.split('-')

    for i in cavespair[n]:
        if i not in cavesname:
            cavesname.add(i)

cavesmap = dict()
templist = list()

for name in cavesname:
    if name == 'end':
        pass
    else: 
        for j in range(len(cavespair)):
            if name in cavespair[j]:
                for adj_caves in cavespair[j]:
                    if adj_caves != name and adj_caves != 'start':
                        templist.append(adj_caves)

        cavesmap[name] = list(templist)
        templist.clear()

def allpossibleroute(map,cave):
    possible_route = list()
    visited = [cave]

    for nextcave in map[cave]:
        visited.append(nextcave)
        explorecave(possible_route,visited,map,nextcave)
        visited.pop()

    routecount = len(possible_route)

    return(routecount)
    
def explorecave(possible_route,visited,map,cave):

    for nextcave in map[cave]:
        if nextcave in visited and nextcave.islower():
            pass

        else:
            visited.append(nextcave)

            if nextcave == 'end':
                possible_route.append(list(visited))

            else:
                explorecave(possible_route,visited,map,nextcave)

            visited.pop()

print(allpossibleroute(cavesmap,'start'))