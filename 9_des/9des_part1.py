import os
from enum import Enum
from math import *
import numpy as np

path = os.getcwd()
data = open(path+'/9_des/input.txt', 'r').readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")

all_head_pos, all_tail_pos = [], []
head_pos_x, head_pos_y = 0, 0
tail_pos_x, tail_pos_y = 0, 0

for direction in data:
    for i in range(int(direction[2:])):
        if direction[0] == "L":
            head_pos_x -= 1
        elif direction[0] == "R":
            head_pos_x += 1
        elif direction[0] == "U":
            head_pos_y -= 1
        elif direction[0] == "D":
            head_pos_y += 1
        head_pos = str(head_pos_x) + " " + str(head_pos_y)
        all_head_pos.append(head_pos)

        if (abs(head_pos_x - tail_pos_x) > 1) or (abs(head_pos_y - tail_pos_y) > 1):
            tail_pos_x += np.sign(head_pos_x-tail_pos_x)
            tail_pos_y += np.sign(head_pos_y-tail_pos_y)
            tail_pos = str(tail_pos_x) + " " + str(tail_pos_y)
            all_tail_pos.append(tail_pos)

tailSet = set(all_tail_pos)

print(f"Part one: {len(tailSet)}")

