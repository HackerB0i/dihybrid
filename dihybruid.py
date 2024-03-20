"""
Description: Dihybrid Cross-breeding Calculator
"""

# input
parent1geno = input("enter parent 1: ")
parent2geno = input("enter parent 2: ")

# make the lists
parent1list = []
parent2list = []

# add alleles to a list
parent1list.append(parent1geno[0] + parent1geno[2])
parent1list.append(parent1geno[1] + parent1geno[2])
parent1list.append(parent1geno[0] + parent1geno[3])
parent1list.append(parent1geno[1] + parent1geno[3])
print(parent1list)

parent2list.append(parent2geno[0] + parent2geno[2])
parent2list.append(parent2geno[1] + parent2geno[2])
parent2list.append(parent2geno[0] + parent2geno[3])
parent2list.append(parent2geno[1] + parent2geno[3])
print(parent2list)

# the punnet square
punnettsquarelist = []
for y in range(4):
    for x in range(4):
        genotype = []
        genotype.append(parent1list[x][0])
        genotype.append(parent2list[y][0])
        genotype.append(parent1list[x][1])
        genotype.append(parent2list[y][1])
        if (parent1list[x][0].islower() and parent2list[y][0].isupper()):
            genotype[0] = parent2list[y][0]
            genotype[1] = parent1list[x][0]
        if (parent1list[x][1].islower() and parent2list[y][1].isupper()):
            genotype[2] = parent2list[y][1]
            genotype[3] = parent1list[x][1]
        punnettsquarelist.append("".join(genotype))

# ratios
phratio = [0,0,0,0]
gratio = [0,0,0,0,0,0,0,0,0]
for i in range(4):
    row = []
    for j in range(4):
        row.append(punnettsquarelist[(i*4)+j])
        if punnettsquarelist[(i*4)+j][0].isupper() and punnettsquarelist[(i*4)+j][2].isupper(): # A?A?
            phratio[0] += 1
            if punnettsquarelist[(i*4)+j][1].isupper() and punnettsquarelist[(i*4)+j][3].isupper(): #AAAA
                gratio[0] += 1
            elif punnettsquarelist[(i*4)+j][1].islower() and punnettsquarelist[(i*4)+j][3].isupper(): #AaAA
                gratio[1] += 1
            elif punnettsquarelist[(i*4)+j][1].islower() and punnettsquarelist[(i*4)+j][3].islower(): #AaAa
                gratio[4] += 1
            elif punnettsquarelist[(i*4)+j][1].isupper() and punnettsquarelist[(i*4)+j][3].islower(): #AAAa
                gratio[3] += 1
        elif punnettsquarelist[(i*4)+j][0].isupper() and punnettsquarelist[(i*4)+j][2].islower(): #A?a?
            phratio[1] += 1
            if punnettsquarelist[(i*4)+j][1].isupper() and punnettsquarelist[(i*4)+j][3].islower(): #AAaa
                gratio[6] += 1
            elif punnettsquarelist[(i*4)+j][1].islower() and punnettsquarelist[(i*4)+j][3].islower(): #Aaaa
                gratio[7] += 1
        elif punnettsquarelist[(i*4)+j][0].islower() and punnettsquarelist[(i*4)+j][2].isupper(): #a?A?
            phratio[2] += 1
            if punnettsquarelist[(i*4)+j][1].islower() and punnettsquarelist[(i*4)+j][3].isupper(): #aaAA
                gratio[2] += 1
            elif punnettsquarelist[(i*4)+j][1].islower() and punnettsquarelist[(i*4)+j][3].islower(): #aaAa
                gratio[5] += 1
        elif punnettsquarelist[(i*4)+j][0].islower() and punnettsquarelist[(i*4)+j][2].islower():
            phratio[3] += 1
            gratio[8] += 1
            
    print(row)
print(gratio)
print(phratio)