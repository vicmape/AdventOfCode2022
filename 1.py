# Advent of Code 2022 - Day 1

file = open('1.txt', 'r')

elf1 = 0
elf2 = 0
elf3 = 0

cur_cal = 0

while True:

    line = file.readline()

    if not line:
        break
    elif line == "\n":
        # I know this is not optimized at all.
        # That's the quick and dirty way of doing it
        if elf1 < elf2:
            if elf1 < elf3:
                if cur_cal > elf1:
                    elf1 = cur_cal
            else:
                if cur_cal > elf3:
                    elf3 = cur_cal
        else:
            if elf2 < elf3:
                if cur_cal > elf2:
                    elf2 = cur_cal
            else:
                if cur_cal > elf3:
                    elf3 = cur_cal
        cur_cal = 0
    else:
        cur_cal += int(line)

print('Top 3 elfs are:')
print('Elf1: ' + str(elf1))
print('Elf2: ' + str(elf2))
print('Elf3: ' + str(elf3))

print('Sum of top elfs is: ' + str(elf1+elf2+elf3))

