with open('D:/Coding Playground/advent of code/Day 14 Polymer/Polymer.txt','r') as file:
    polymer = file.read().split('\n\n')

template = polymer[0]
insertion = polymer[1].split('\n')

for i, n in enumerate(insertion):
    insertion[i] = n.split(' -> ')

def polymerization(initial,rule,step):

    for i in range(step):

        for j in range(len(initial)-1):
            polypair = initial[2*j:2*j+2]

            for k in range(len(rule)):

                if polypair in rule[k]:
                    
                    initial = initial[:2*j+1] + rule[k][1] + initial[2*j+1:]
    
    return(dissectpolymer(initial))

def dissectpolymer(finalchain):
    unique = sorted(set([element for element in finalchain]))
    ele_count = list()

    for element in unique:
        temp_count =0

        for atom in finalchain:
            if element == atom:
                temp_count+= 1
        
        ele_count.append(temp_count)

    difference = max(ele_count) - min(ele_count)

    return(dict(zip(unique,ele_count)))

print(polymerization(template,insertion,10))
