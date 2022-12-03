from enum import Enum
import os
path = os.getcwd()
class Hand1(Enum):
    A = 1
    B = 2
    C = 3
class Hand2(Enum):
    X = 1
    Y = 2
    Z = 3
data = open(path + '/2_des/input.txt', 'r').readlines()
points = 0
partTwoPoints = 0
for elem in data:
    round = elem.strip("\n").replace(" ", "")
    if(round[1] == Hand2.X.name):
        if round[0] == Hand1.A.name:
            points += 3
            partTwoPoints += 3
        elif round[0] == Hand1.C.name:
            points += 6
            partTwoPoints += 2
        else:
            partTwoPoints += 1
        points += Hand2.X.value
    elif(round[1] == Hand2.Y.name):
        if(round[0] == Hand1.B.name):
            points += 3
            partTwoPoints += Hand1.B.value
        elif(round[0] == Hand1.A.name):
            points += 6
            partTwoPoints += Hand1.A.value
        else:
            partTwoPoints += Hand1.C.value
        points += Hand2.Y.value
        partTwoPoints += 3
    else:
        if(round[0] == Hand1.C.name):
            points += 3
            partTwoPoints += 1
        elif(round[0] == Hand1.B.name):
            points += 6
            partTwoPoints += 3
        else:
            partTwoPoints += 2
        points += Hand2.Z.value
        partTwoPoints += 6

print(f"Part one: {points}")
print(f"Part two: {partTwoPoints}")

