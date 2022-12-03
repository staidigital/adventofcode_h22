import os
path = os.getcwd()
itemTypes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rucksacks = open(path + '/3_des/input.txt','r').readlines()
prioritySum = 0
for rucksack in rucksacks:
    rucksack = rucksack.strip('\n')
    comp1 = set(rucksack[0:int(len(rucksack)/2)])
    comp2 = set(rucksack[int(len(rucksack)/2):])
    sameType = comp1.intersection(comp2)
    priority = itemTypes.find(sameType.pop())+1
    prioritySum += priority
print(f'Part one: {prioritySum}')

identifierSum = 0
for i in range(0,len(rucksacks)-1,3):
    elfOne, elfTwo, elfThree = set(rucksacks[i].strip('\n')),set(rucksacks[i+1].strip('\n')), set(rucksacks[i+2].strip('\n'))
    identifier = elfOne.intersection(elfTwo).intersection(elfThree)
    identifierSum += itemTypes.find(identifier.pop())+1
print(f'Part two: {identifierSum}')
