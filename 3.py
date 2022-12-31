# https://adventofcode.com/2022/day/3

def get_letter_val(x):
    offset = (ord('a') - 1) if x.islower() else (ord('A') - 27)
    return (ord(x) - offset)

with open('3.txt', 'r') as f: data = f.read().split()

# Part 1

rucks = []
for ruck in data:
    n = len(ruck) // 2
    rucks.append([ruck[:n], ruck[n:]])

letters = []
for r1, r2 in rucks:
    intersection_list = list(set(r1) & set(r2))
    letters.append(intersection_list[0])

print('Part 1:', sum(get_letter_val(l) for l in letters))

# Part 2

badges = []
n_groups = len(data)//3
for i in range(n_groups):
    group = data[i*3:(i+1)*3]
    a,b,c = group
    badge = list(set(a) & set(b) & set(c))
    badges.append(badge[0])

print('Part 2:', sum(get_letter_val(b) for b in badges))