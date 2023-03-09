# Classes

# Clues for task :
# A,X - Rock B,Y- Paper C,Z-scissors

# This is version for second part of this task becouse
# X - Lose Y - Draw Z - Win

def calculating_Win(guide):
    x = guide[2]
    if guide[0] == 'A':
        match x:
            case 'X':
                return 3+0
            case 'Y':
                return 1+3
            case 'Z':
                return 6+2

    elif guide[0] == 'B':
        match guide[2]:
            case 'X':
                return 1+0
            case 'Y':
                return 2+3
            case 'Z':
                return 3+6


    elif guide[0] == 'C':
        match guide[2]:
            case 'X':
                return 2+0
            case 'Y':
                return 3+3
            case 'Z':
                return 1+6


def calculating_Choice(guide):

    match guide[2]:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3



# Getting data
with open("Zadanie2_input.txt") as f:
    lines = f.readlines()

sum = 0

for line in lines:
    sum = sum + calculating_Win(line)

print(sum)


# The answer to the first question was : 10994