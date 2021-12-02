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

    print(movement)
    print(depth)
    print(hor)

print(depth*hor)
    