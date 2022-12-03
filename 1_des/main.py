f = open("data.txt","r")
lines = f.readlines()

allElves = []
tempList = []
caloriesPerElf = []

for line in lines:
    line = line.strip('\n')
    if line != '':
        tempList.append(int(line))
    else: 
        allElves.append(tempList)
        tempList = []

for elf in allElves:
    thisElfCalories = 0
    for food in elf:
        thisElfCalories += food
    caloriesPerElf.append(thisElfCalories)

sortedCaloriesPerElves = sorted(caloriesPerElf)

print(f'Alven med flest calorier hadde med seg {sortedCaloriesPerElves[-1]} kalorier')
print(f'De tre med mest kalorier har til sammen {sortedCaloriesPerElves[-1] + sortedCaloriesPerElves[-2] + sortedCaloriesPerElves[-3]} kalorier' )
