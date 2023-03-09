def Part1(lines):
    i = 0
    while i < len(lines):
        if i >3:
            IsDoubled = False
            pattern = lines[i-4:i]
            for char in pattern:
                if pattern.count(char) >= 2:
                    IsDoubled = True
                    break
                else:
                    IsDoubled = False

            if not IsDoubled:
                return i

        i+= 1

def Part2(lines):
    i = 0
    while i < len(lines):
        if i >13:
            IsDoubled = False
            pattern = lines[i-14:i]
            for char in pattern:
                if pattern.count(char) >= 2:
                    IsDoubled = True
                    break
                else:
                    IsDoubled = False

            if not IsDoubled:
                return i

        i+= 1

with open("Zadanie6_Input.txt") as f:
    lines = f.readlines()

line = lines[0]
print("1 Part: "+str(Part1(line)))  # The correct answer was 1175
print("2 Part: "+str(Part2(line)))  # The correct answer was 3217

