import os
path = os.getcwd()
data = open(path+'/10_des/input.txt', 'r').readlines()

cycles = []
for i in range(len(data)):
    data[i] = data[i].strip("\n")
for i in range(240):
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

print("Part one: " + str(cycles[19]*20 + cycles[59]*60 + cycles[99]*100 + cycles[139]*140 + cycles[179]*180 + cycles[219]*220))