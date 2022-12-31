# https://adventofcode.com/2022/day/2

with open('1.txt', 'r') as f: data = f.read()

data = data.split('\n\n')

rows = [row.split() for row in data]

totals = [sum([int(i) for i in row]) for row in rows]

totals.sort()

# Part 1 answer
print(totals[-1])

# Part 2 answer
print(sum(totals[-3:]))
