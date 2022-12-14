import os
path = os.getcwd()
data = open(path+'/10_des/input.txt', 'r').readlines()

cycles = []
for i in range(len(data)):
    data[i] = data[i].strip("\n")
for i in range(241):
    cycles.append(1)
x = 1
counter = 0
for i in range(len(data)):
    if data[i][:4] == "addx":
        counter += 2
        x += int(data[i][5:])
    elif data[i][:4] == "noop":
        counter += 1
    for j in range(counter, len(cycles)):
        cycles[j] = x
currentLine = ""
charCount = 0
spritePos = 1
for i in range(241):
    spritePos = cycles[i]
    if spritePos + 1 == charCount or spritePos - 1 == charCount or spritePos == charCount:
        currentLine += "#"
    else:
        currentLine += "."
    if ((i+1) % 40 == 0 and i != 0):
        print(currentLine)
        currentLine = ""
        charCount = 0
    else:
        charCount += 1
