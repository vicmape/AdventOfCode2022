# Advent of Code 2022 - Day 4

import re

count = 0
with open('4.txt', 'r') as fp:
    for line in fp:
        res = re.findall(r'\d+', line)
        res = list(map(int, res))
        if (res[0] <= res[2] and res[1] >= res[3]) or (res[2] <= res[0] and res[3] >= res[1]):
            count += 1
print("full overlap: " + str(count))

count = 0
with open('4.txt', 'r') as fp:
    for line in fp:
        res = re.findall(r'\d+', line)
        res = list(map(int, res))

        if ((res[0] >= res[2] and res[0] <= res[3]) or\
            (res[1] >= res[2] and res[1] <= res[3]) or\
            (res[2] >= res[0] and res[2] <= res[1]) or\
            (res[3] >= res[0] and res[3] <= res[1])):
            count += 1

print("overlap: " + str(count))