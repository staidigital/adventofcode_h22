import os
path = os.getcwd()
data = open(path+'/7_des/input.txt', 'r').readlines()
filesystem = {}
currentFolder = filesystem
folderPath = []

for command in data:
    command = command.strip("\n")
    if command[0] == "$":
        if command[2:4] == "cd":
            if command[5] == "/":
                currentFolder = filesystem
            elif command[5:7] == "..":
                currentFolder = folderPath.pop()
            else:
                folderPath.append(currentFolder)
                currentFolder = currentFolder[command[5:]]
        elif command[2:4] == "ls":
            continue
    elif command[0:3] == "dir":
        currentFolder[command[4:]] = {}
    elif command[0].isdigit():
        filesize, filename = command.split(" ")
        currentFolder[filename] = filesize
        if "totalFilesize" in currentFolder:
            tempFilesize = int(currentFolder["totalFilesize"])
            tempFilesize += int(filesize)
            currentFolder["totalFilesize"] = tempFilesize
        else:
            currentFolder["totalFilesize"] = filesize
        for folder in folderPath:
            if "totalFilesize" in folder:
                tempFilesize = int(folder["totalFilesize"])
                tempFilesize += int(filesize)
                folder["totalFilesize"] = tempFilesize
            else:
                folder["totalFilesize"] = filesize

totalFolderSizes = 0
allFolderSizes = []

def traverseDict(a):
    global totalFolderSizes, allFolderSizes
    if isinstance(a,dict):
        if int(a["totalFilesize"]) < 100000:
            totalFolderSizes += int(a["totalFilesize"])
        allFolderSizes.append(int(a["totalFilesize"]))
        for item in a.values():
            traverseDict(item)

traverseDict(filesystem)
print(f"Part one: {totalFolderSizes}")

diskSpace = 70000000
neededDiskSpace = 30000000
idealFolderSize = 0
allFolderSizes.sort()

for size in allFolderSizes:
    if diskSpace - int(filesystem["totalFilesize"]) + size > neededDiskSpace:
        idealFolderSize = size
        break

print(f"Part two: {idealFolderSize}")