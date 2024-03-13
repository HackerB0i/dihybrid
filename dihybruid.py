"""
Description: Dihybrid Cross-breeding Calculator
"""

parent1geno = input("enter p1: ")
parent2geno = input("enter p2: ")

parent1list = []
parent2list = []

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

punnettsquarelist = []
for x in range(4):
    for y in range(4):
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
        punnettsquarelist.append(genotype)

ratio = [0,0,0,0]
for i in range(4):
    row = []
    for j in range(4):
        row.append(punnettsquarelist[(i*4)+j])
        if punnettsquarelist[(i*4)+j][0].isupper() and punnettsquarelist[(i*4)+j][2].isupper():
            ratio[0] += 1
        elif punnettsquarelist[(i*4)+j][0].isupper() and punnettsquarelist[(i*4)+j][2].islower():
            ratio[1] += 1
        elif punnettsquarelist[(i*4)+j][0].islower() and punnettsquarelist[(i*4)+j][2].isupper():
            ratio[2] += 1
        else:
            ratio[3] += 1
            
    print(row)

print(ratio)