"""
Name: Dihybrid Cross program
"""

parent1geno = input("enter p1: ")
parent2geno = input("enter p2: ")

parent1list = []
parent2list = []

parent1list.append(parent1geno[0] + parent1geno[2])
parent1list.append(parent1geno[0] + parent1geno[3])
parent1list.append(parent1geno[1] + parent1geno[2])
parent1list.append(parent1geno[1] + parent1geno[3])

parent2list.append(parent2geno[0] + parent2geno[2])
parent2list.append(parent2geno[0] + parent2geno[3])
parent2list.append(parent2geno[1] + parent2geno[2])
parent2list.append(parent2geno[1] + parent2geno[3])

punnettsquarelist = []
for i in range(16):
    punnettsquarelist.append()

for x in range(4):
    for y in range(4):
        genotype = parent1list[x][0] + parent2list[y][0]