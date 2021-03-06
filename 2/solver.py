#Link to challenge: https://adventofcode.com/2021/day/2
import os
lines = []
with open(os.getcwd() + '\\2\\input.txt') as f:
    lines = f.readlines()

hor = 0
depth = 0

for i in range(0, len(lines)):
    movement = lines[i].strip().split()
    direction = movement[0]
    value = int(movement[1])

    if(direction == "forward"):
        hor += value
    elif(direction == "down"):
        depth += value
    elif(direction == "up"):
        depth -= value

print(depth*hor)
    
aim = 0
hor = 0
depth = 0

#[part 2]
for i in range(0, len(lines)):
    movement = lines[i].strip().split()
    direction = movement[0]
    value = int(movement[1])

    if(direction == "forward"):
        hor += value
        depth += aim*value
    elif(direction == "down"):
        aim += value
    elif(direction == "up"):
        aim -= value

print(depth*hor)