
class Line:

    def __init__(self):
        self.content = list()

    def Add(self,a):
        self.content.append(a)

    def Delete(self):
        return self.content.pop()

class Stack:

    def __init__(self):
        self.lines = []

    def AddLine(self):
        l = Line()
        self.lines.append(l)

    def Move(self,amount,fromm,to):
        temp = list()
        for i in range(int(amount)):
            temp.append(self.lines[int(fromm)-1].Delete())
        temp.reverse()
        for j in temp:
            self.lines[int(to)-1].Add(j)

# Getting data

with open("Zadanie5_Input.Txt") as f:
    lines = f.readlines()

# So I need to create the stack manually :(
stack = Stack()
for i in range(9):
    stack.AddLine()
#region Creating Stack


stack.lines[0].Add("J")
stack.lines[0].Add("H")
stack.lines[0].Add("G")
stack.lines[0].Add("M")
stack.lines[0].Add("Z")
stack.lines[0].Add("N")
stack.lines[0].Add("T")
stack.lines[0].Add("F")

stack.lines[1].Add("V")
stack.lines[1].Add("W")
stack.lines[1].Add("J")

stack.lines[2].Add("G")
stack.lines[2].Add("V")
stack.lines[2].Add("L")
stack.lines[2].Add("J")
stack.lines[2].Add("B")
stack.lines[2].Add("T")
stack.lines[2].Add("H")

stack.lines[3].Add("B")
stack.lines[3].Add("P")
stack.lines[3].Add("J")
stack.lines[3].Add("N")
stack.lines[3].Add("C")
stack.lines[3].Add("D")
stack.lines[3].Add("V")
stack.lines[3].Add("L")

stack.lines[4].Add("F")
stack.lines[4].Add("W")
stack.lines[4].Add("S")
stack.lines[4].Add("M")
stack.lines[4].Add("P")
stack.lines[4].Add("R")
stack.lines[4].Add("G")

stack.lines[5].Add("G")
stack.lines[5].Add("H")
stack.lines[5].Add("C")
stack.lines[5].Add("F")
stack.lines[5].Add("B")
stack.lines[5].Add("N")
stack.lines[5].Add("V")
stack.lines[5].Add("M")

stack.lines[6].Add("D")
stack.lines[6].Add("H")
stack.lines[6].Add("G")
stack.lines[6].Add("M")
stack.lines[6].Add("R")

stack.lines[7].Add("H")
stack.lines[7].Add("N")
stack.lines[7].Add("M")
stack.lines[7].Add("V")
stack.lines[7].Add("Z")
stack.lines[7].Add("D")

stack.lines[8].Add("G")
stack.lines[8].Add("N")
stack.lines[8].Add("F")
stack.lines[8].Add("H")

#endregion Creating Stack


# Program

for line in lines:
    string = ""
    i=0
    while i < len(line):
        if line[i] =="":
            i+=1
            continue
        if i+1<len(line):
            if line[i].isdigit() and line[i+1].isdigit():
                string += line[i] + line[i+1]
                i = i+2
                continue

        if line[i].isdigit():
            string += line[i]
        i+=1
    if len(string) == 3:
        stack.Move(string[0],string[1],string[2])
    else:
        stack.Move((string[0]+string[1]),string[2],string[3])

temp = ""
for i in stack.lines:
    temp += i.Delete()
print(temp)

# Answer to first puzzle was TDCHVHJTG
