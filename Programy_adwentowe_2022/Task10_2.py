
class Screen:

    def __init__(self):
        self.display = []
        self.filling_display()
        self.numberOfRows = 0

    def filling_display(self):
        for i in range(6):
            row = []
            for j in range(40):
                row.append('.')
            self.display.append(row)

    def isToDraw(self,x, cycle_counter):
        intervalOf_sprite = []
        # So the X indicates the middle sprite position so i make an interval of <x-1,x+1>
        for i in range(x-1,x+2):
            intervalOf_sprite.append(i)
        # Now with this interval i will check if the current CRT is being in it
        if cycle_counter in intervalOf_sprite:
            return True
        else:
            return False

    def adjusting_cycle(self,cycle_counter):
        # The vertical position doesnt matter so i need the cycle counter to be <40 all the time
        result = cycle_counter
        if cycle_counter > 40:
            result -= 40
            self.numberOfRows+=1

        if self.numberOfRows > 6:
            result = -1000000
        # So after i make 6 rows i dont want the program to work so i set it to this value and its impossible to recover from this

        return result

    def draw(self,x,cycle_counter):
        cycle_counter = self.adjusting_cycle(cycle_counter)

        if self.isToDraw(x,cycle_counter):
            self.display[self.numberOfRows][cycle_counter-1] = '#'

        return cycle_counter

    def out(self):
        for row in self.display:
            for char in row:
                print(char,end=" ")
            print("\n",end="")



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
x = 1
i = 0
screen = Screen()
toSkip = False

while i < len(lines):

    # so i need to skip this if we are after the ap.. operation
    if not toSkip:
        oper,valueof_oper = gettingData(lines[i])

    if oper == "noop":
        i += 1
        cycles_counter = screen.draw(x,cycles_counter)
        cycles_counter += 1
        wascalculated = False

    elif oper == "addx" and toSkip is False:
        cycles_counter = screen.draw(x,cycles_counter)
        cycles_counter +=1
        toSkip = True

    elif oper == "addx" and toSkip is True:
        cycles_counter = screen.draw(x,cycles_counter)
        cycles_counter += 1
        toSkip = False
        x += valueof_oper
        i += 1


screen.out()



