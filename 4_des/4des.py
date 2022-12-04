import os
path = os.getcwd()
data = open(path+'/4_des/input.txt').readlines()
containedCounter, overlapCounter = 0, 0
for entry in data:
    elfPair = entry.strip("\n")
    elfOne, elfTwo = elfPair.split(",")
    elfOneMin, elfOneMax = [int(s) for s in elfOne.split("-")]
    elfTwoMin, elfTwoMax = [int(s) for s in elfTwo.split("-")]
    if(elfOneMin <= elfTwoMin and elfOneMax >= elfTwoMax):
        containedCounter += 1
        overlapCounter += 1
    elif (elfTwoMin <= elfOneMin and elfTwoMax >= elfOneMax):
        containedCounter += 1
        overlapCounter += 1
    elif((elfOneMin <= elfTwoMin <= elfOneMax) or (elfOneMin <= elfTwoMax <= elfOneMax)):
        overlapCounter += 1
print(f'Del 1: {containedCounter}')
print(f'Del 2: {overlapCounter}')