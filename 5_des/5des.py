import os, copy
path = os.getcwd()
data = open(path + "/5_des/input.txt").readlines()
stack = [[] for i in range(0,9)]
#Lager liste av stack
for i in range(8):
    row = data[i].strip("\n")
    for j in range(0,35,4):
        stackIndex = int(j/4)
        if j < 34:
            stack[stackIndex].append(row[j+1])

#Fjerner tomme elementer fra listene
for row in stack:
    for i in range(len(row)):
        try:
            row.remove(" ")
        except:
            continue

#Gjennomfører sorteringen
data = data[10:]
for i in range(len(stack)):
    stack[i].reverse()
backupStack = copy.deepcopy(stack)
for entry in data:
    entry = entry.strip("\n")
    entryList = entry.split(" ")
    numberToMove, fromStack, toStack = int(entryList[1]), int(entryList[3]), int(entryList[5])
    for i in range(numberToMove):
        stack[toStack-1].append(stack[fromStack-1].pop())
topItems = ""
for i in range(0,len(stack)):
    topItems += stack[i][-1]
print(f"Part 1: {topItems}")

# Part two
for entry in data:
    entry = entry.strip("\n")
    entryList = entry.split(" ")
    numberToMove,fromStack, toStack = int(entryList[1]), int(entryList[3]), int(entryList[5])
    backupStack[toStack-1].extend(backupStack[fromStack-1][-numberToMove:])
    backupStack[fromStack-1] = backupStack[fromStack-1][0:-numberToMove]
partTwoTopItems = ""
for i in range(0,len(backupStack)):
    partTwoTopItems += backupStack[i][-1]
print(f"Part 2: {partTwoTopItems}")

