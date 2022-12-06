import os, copy
path = os.getcwd()
data = open(path + "/6_des/input.txt").readlines()[0]
##Part one
packetMarker = None
index = 0
while packetMarker == None:
    fourGroup = set(data[index:index+4])
    if(len(fourGroup) == 4):
        packetMarker = index + 4
        print(f"Start-of-packet marker is {packetMarker}")
    index += 1

#Part two
messageMarker = None
while messageMarker == None:
    fourGroup = set(data[index:index+14])
    if(len(fourGroup) == 14):
        messageMarker = index + 14
        print(f"Start-of-message marker is {messageMarker}")
    index += 1