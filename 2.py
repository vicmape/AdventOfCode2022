# https://adventofcode.com/2022/day/2

'''
            OPPONENT       YOU      POINTS
Rock            A           X          1
Paper           B           Y          2
Scissors        C           Z          3

0 - Loose
3 - Draw
6 - Win
'''

res_map1 = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3}
}
res_map2 = {
    'A': {'A':3, 'B':6, 'C':0},
    'B': {'A':0, 'B':3, 'C':6},
    'C': {'A':6, 'B':0, 'C':3},
}

base_map1 = {'X': 1, 'Y': 2, 'Z': 3}

base_map2 = {'A': 1, 'B': 2, 'C': 3}

translation_map = {
    'A': {'X':'C', 'Y':'A', 'Z':'B'},
    'B': {'X':'A', 'Y':'B', 'Z':'C'},
    'C': {'X':'B', 'Y':'C', 'Z':'A'},
}

with open('2.txt', 'r') as f: data = f.read()

data = data.split('\n')[:-1]

rows = [row.split(' ') for row in data]

# Part 1

base1 = sum([base_map1[j] for i,j in rows])

res1 = sum([res_map1[i][j] for i,j in rows])

print('Part 1:', base1 + res1)

# Part 2 

translation = [[i, translation_map[i][j]] for i,j in rows]

base2 = sum([base_map2[j] for i,j in translation])

res2 = sum([res_map2[i][j] for i, j in translation])

print('Part 2:', base2 + res2)
