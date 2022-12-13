import os
path = os.getcwd()
data = open(path+'/8_des/input.txt', 'r').readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")
    
def checkVisibiltyRow(someString):
    visibleTrees = ""
    for i in range(len(someString)-1):
        if i == 0:
            coords = "0"
            visibleTrees += coords
            continue
        trees = list(int(s) for s in someString[:i])
        treesSorted = sorted(trees)
        if int(someString[i]) > treesSorted[-1]:
            coords = " " + str(i) 
            visibleTrees += coords
        else: continue
    return visibleTrees


def checkVisibilityGrid(someList):
    dataTopDown = list(map(''.join, zip(*someList)))
    foundTrees = []
    for i in range(len(someList)):
        row = someList[i]
        treesInRow = checkVisibiltyRow(row).split(" ")
        for tree in treesInRow:
            coord = str(i) + " " + tree
            foundTrees.append(coord)
    for i in range(len(someList)):
        row = someList[i][::-1]
        treesInRow = checkVisibiltyRow(row).split(" ")
        #print(treesInRow)
        for tree in treesInRow:
            coord = str(i) + " " + str(len(row) - 1 - int(tree))
            foundTrees.append(coord)
    for i in range(len(someList)):
        row = dataTopDown[i]
        treesInRow = checkVisibiltyRow(row).split(" ")
        #print(treesInRow)
        for tree in treesInRow:
            coord = tree + " " + str(i)
            foundTrees.append(coord)
    for i in range(len(someList)):
        row = dataTopDown[i][::-1]
        treesInRow = checkVisibiltyRow(row).split(" ")
        #print(treesInRow)
        for tree in treesInRow:
            coord = str(len(row)-1 -int(tree)) + " " + str(i)
            foundTrees.append(coord)
    return foundTrees

trees = checkVisibilityGrid(data)

treeSet = set(trees)
print(f"Part 1: {len(treeSet)}")

#Part two
x_min, y_min = 0, 0
x_max, y_max = 98, 98
viewMax = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        r_count, l_count, u_count, d_count = 1, 1, 1, 1
        foundEdgeR, foundEdgeL, foundEdgeUp, foundEdgeDown = False, False, False, False
        while not foundEdgeR:
            if j + r_count < x_max:
                if data[i][j] > data[i][j + r_count]:
                    r_count += 1
                else:
                    foundEdgeR = True
            else:
                foundEdgeR = True
        while not foundEdgeL:
            if j - l_count > x_min:
                if data[i][j] > data[i][j - l_count]:
                    l_count += 1
                else:
                    foundEdgeL = True
            else:
                foundEdgeL = True
        while not foundEdgeUp:
            if i - u_count > y_min:
                if data[i][j] > data[i - u_count][j]:
                    u_count += 1
                else:
                    foundEdgeUp = True
            else:
                foundEdgeUp = True
        while not foundEdgeDown:
            if i + d_count < y_max:
                if data[i][j] > data[i + d_count][j]:
                    d_count += 1
                else:
                    foundEdgeDown = True
            else:
                foundEdgeDown = True
        currentView = r_count * l_count * u_count * d_count
        if currentView > viewMax:
            viewMax = currentView

print(f"Part 2: {viewMax}")