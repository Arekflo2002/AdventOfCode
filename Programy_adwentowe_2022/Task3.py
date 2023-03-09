
# // Zamiana z litery na parytet(z tablicy ASCII) :
        # // Male : 'Litera' - 96
        # // Duze : 'Litera' - 38

def Calculate(result):
    if result.islower():
        return int(ord(result)-96)
    else:
        return int(ord(result) - 38)

def searching_letter(stri):
    stri_1 = stri[:int(len(stri) / 2)]
    stri_2 = stri[int(len(stri) / 2):]

    result = ""

    for letter in stri_1:
        if letter in stri_2:
            return letter

def thelongeststring(str1,str2,str3):

    if len(str1) >= len(str2) and  len(str1) >= len(str3):
        return str1,str2,str3

    elif len(str2) >= len(str3) and len(str2) >= len(str1):
        return str2,str1,str3

    else:
        return str3,str2,str1

def searching_badge(str1,str2,str3):
    str1,str2,str3 = thelongeststring(str1,str2,str3)
    for letter1 in str1:
        if letter1 in str2:
            if letter1 in str3:
                print(letter1)
                return Calculate(letter1)


# Getting Data
with open("Zadanie3_Input.txt") as f:
    lines = f.readlines()

sum = 0
for i in range(0,int(len(lines)),3):
    sum+=searching_badge(lines[i],lines[i+1],lines[i+2])

# The correct answer to first part is 7674
print(sum)
