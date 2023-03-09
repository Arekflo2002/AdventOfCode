
# Getting data from file

# Classes needed to get the program working

class Elf:

    def __init__(self):
        self.calories = 0

    def Add_calories(self,cal):
        self.calories += cal

class Bunch_elves:

    def __init__(self):
        self.bunch = []

    def Add_elf(self):
        elf = Elf()
        self.bunch.append(elf)

    def Add_calories(self,index,calories):
        self.bunch[index].Add_calories(calories)

    def Searching_Max_Calories(self):
        # So to do second part of this task i have to remove top elves so i will do it :(
        maximum = max(self.bunch, key=lambda e: e.calories).calories
        # self.bunch = list(filter(lambda e: e.calories != maximum,self.bunch))
        self.bunch.remove(max(self.bunch,key=lambda e:e.calories))   # There is second version of what is above
        return maximum



#  Getting Data from file
with open('Zadanie1_input.txt') as f:
    lines = f.readlines()

# Program

elves_counter = 0
bunch = Bunch_elves()
bunch.Add_elf()

for line in lines:
    if line == "\n":
        bunch.Add_elf()
        elves_counter+=1
    else:
        bunch.Add_calories(elves_counter,int(line))

Top=0
Top += bunch.Searching_Max_Calories()
Top += bunch.Searching_Max_Calories()
Top += bunch.Searching_Max_Calories()

print(Top)

