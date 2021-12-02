#Link to challenge: https://adventofcode.com/2021/day/1

import os

lines = []
with open(os.getcwd() + '\\1\\input.txt') as f:
    lines = f.readlines()

count = 0
previous_number = int(lines[0].strip())

for i in range(1, len(lines)):
    if int(lines[i].strip()) > previous_number:
        count = count + 1
    previous_number = int(lines[i].strip())

print("Total number of increases: " + str(count))
    