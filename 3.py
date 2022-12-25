# Advent of Code 2022 - Day 3

sum = 0

# Part 1
with open('3.txt') as fp:
    for line in fp:

        half = len(line)//2
        second = line[half:]

        for letter in line:
            res = second.find(letter)
            if res != -1:
                if letter.islower():
                    prio = ord(letter) - ord('a') + 1
                else:
                    prio = ord(letter) - ord('A') + 27
                sum += prio
                break

print('The sum of all prio objects is: ' + str(sum))

# Part 2
with open('3.txt') as fp:
    elf1 = 0
    elf2 = 0
    elf3 = 0
    sum = 0
    for line in fp:
        if elf1 == 0:
            elf1 = line
        elif elf2 == 0:
            elf2 = line
        else:
            elf3 = line
            for letter in elf1:
                res = elf2.find(letter)
                if res != -1:
                    res = elf3.find(letter)
                    if res != -1:
                        if letter.islower():
                            prio = ord(letter) - ord('a') + 1
                        else:
                            prio = ord(letter) - ord('A') + 27

                        sum += prio
                        break
            # Reset elfs
            elf1 = elf2 = elf3 = 0

print("sum of badges: " + str(sum))

