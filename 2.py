# Advent of Code 2022 - Day 2
'''
            OPPONENT       YOU      POINTS
Rock            A           X          1
Paper           B           Y          2
Scissors        C           X          3

0 - Loose
3 - Draw
6 - Win
'''

score = 0

# Part 1
with open('2.txt') as fp:
    for line in fp:
        round = line.split()

        match round[0]:
            case 'A':
                match round[1]:
                    case 'X':
                        score += 3 # Draw
                        score += 1 # for choosing rock
                    case 'Y':
                        score += 6 # Win
                        score += 2 # for choosig paper
                    case 'Z':
                        score += 0 # Loose
                        score += 3 # for choosig scissors
            case 'B':
                match round[1]:
                    case 'X':
                        score += 0 # Loose
                        score += 1 # for choosing rock
                    case 'Y':
                        score += 3 # Draw
                        score += 2 # for choosig paper
                    case 'Z':
                        score += 6 # Win
                        score += 3 # for choosig scissors
            case 'C':
                match round[1]:
                    case 'X':
                        score += 6 # Win
                        score += 1 # for choosing rock
                    case 'Y':
                        score += 0 # Loose
                        score += 2 # for choosig paper
                    case 'Z':
                        score += 3 # Draw
                        score += 3 # for choosig scissors

print ('My total score (part 1) is: ' + str(score))

# Part 2
# X I need to loose
# Y I need to draw
# Z I need to win

score = 0

with open('2.txt') as fp:
    for line in fp:
        round = line.split()

        match round[1]:
            # Loose
            case 'X':
                score += 0
                match round[0]:
                    case 'A':
                        score +=3
                    case 'B':
                        score +=1
                    case 'C':
                        score +=2

            # Draw
            case 'Y':
                score += 3
                match round[0]:
                    case 'A':
                        score +=1
                    case 'B':
                        score +=2
                    case 'C':
                        score +=3

            # Win
            case 'Z':
                score += 6
                match round[0]:
                    case 'A':
                        score +=2
                    case 'B':
                        score +=3
                    case 'C':
                        score +=1

print ('My total score (part 2) is: ' + str(score))