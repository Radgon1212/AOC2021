with open('D:/Coding Playground/advent of code/Day 14 Polymer/Polymer.txt','r') as file:
    polymer = file.read().split('\n\n')

template = polymer[0]
insertion = polymer[1].split('\n')
insertionMap = dict()

for i, n in enumerate(insertion):
    insertion[i] = n.split(' -> ')

for [key,value] in insertion:
    insertionMap[key] = value
    #rule/ mapping for polypair to created atom

def polymerization(initChain, insertRule, steps):
    #initChain = string
    #insertRule = dict(pair, childElement)
    #steps = integer

    uniqueMap = dict()
    insertRulePairs = dict()
    pairsCount = dict()
    
    for atom in initChain:
        uniqueMap[atom] = uniqueMap.get(atom,0) + 1

    for parent in insertRule:
        pairsCount[parent] = pairsCount.get(parent,0)
        #craft dictionary for each possible parent pair

        atom = insertRule[parent]
        uniqueMap[atom] = uniqueMap.get(atom,0)
        #craft dictionary for each possible unique atom

        insertRulePairs[parent] = parent[0]+atom, atom+parent[1] 
        #craft dictionary for parent pair to point to child pairs

    tempPairsCount = dict(pairsCount)
    childPairsCount = dict(pairsCount)

    for i in range(len(initChain)-1):
        polyPair = initChain[i:i+2]
        #pull out pair to analyse
        tempPairsCount[polyPair] += 1

    for j in range(steps):
        for parent in pairsCount:
            childPairsCount[parent] = int(tempPairsCount[parent])
            pairsCount[parent] += childPairsCount[parent]
            tempPairsCount[parent] = 0

        for parent in pairsCount:
            for childPair in insertRulePairs[parent]:
                tempPairsCount[childPair] += childPairsCount[parent]

    for parent in pairsCount:
        atom = insertRule[parent]
        uniqueMap[atom] += pairsCount[parent]

    atomcount = uniqueMap.values()
    highest = max(atomcount)
    lowest = min(atomcount)

    return(highest-lowest)

print(polymerization(template,insertionMap,40))