

def gettingData(string):
    oper = ""
    value = ""
    isoper = True
    for char in string:
        if not char.isspace():
            if isoper:
                oper += char
            else:
                value += char
        else:
            isoper = False

    value_without_sign = value
    if value != "":
        sign = 0
        if value[0] == '-':
            value_without_sign = value[1:]
            sign = 1



        if sign:
            if len(value) == 1:
                value = int(value_without_sign)
            else:
                value = int(value_without_sign)
            value = -value
        else:
            if len(value) ==1:
                value = int(value)
            else:
                value = int(value)
    else:
        value = 0

    return oper,value



with open("Zadanie10_Input.txt") as f:
    lines = f.readlines()

cycles_counter = 0
cycles_multiplier = [20,60,100,140,180,220]
x = 1
i = 0
signal_strength = 0
toSkip = False
wascalculated = False

while i < len(lines):
    if cycles_counter in cycles_multiplier and not wascalculated:
        signal_strength += (x*cycles_counter)
        wascalculated = True
    # so i need to skip this if we are after the ap.. operation
    if not toSkip:
        oper,valueof_oper = gettingData(lines[i])
    if oper == "noop":
        i += 1
        cycles_counter += 1
        wascalculated = False

    elif oper == "addx" and toSkip is False:
        cycles_counter +=1
        wascalculated = False
        toSkip = True

    elif oper == "addx" and toSkip is True:
        cycles_counter += 1
        wascalculated = False

        if cycles_counter in cycles_multiplier and not wascalculated:
            signal_strength += (x * cycles_counter)
            wascalculated = True
        toSkip = False
        x += valueof_oper
        i += 1



print(signal_strength)



