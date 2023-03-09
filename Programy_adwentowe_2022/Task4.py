
class Assignment:

    def __init__(self,line):
        temp = line.split(',')
        temp1 = self.Getting_values(temp[0])
        self.start,self.stop= temp1[0],temp1[1]

        temp2 = self.Getting_values(temp[1])
        self.start1,self.stop1 = temp2[0],temp2[1]


    def Getting_values(self,elf):
        ass = elf.split('-')
        start = int(ass[0])
        stop = int(ass[1])

        start1 = int(ass[0])
        stop1 = int(ass[1])
        return start,stop,start1,stop1

    def Is_covering_all(self):
        if (self.stop1>=self.stop and self.start1<=self.start) or (self.stop>=self.stop1 and self.start<=self.start1):
            return 1
        else:
            return 0

    def Is_coverring_at_all(self):
        if (self.start1 > self.stop) or (self.start>self.stop1):
            return 0
        else:
            return 1


with open("Zadanie4_Input.txt") as f:
    lines = f.readlines()

sum = 0
ass = Assignment(lines[2])
print(ass.start,ass.stop)
for line in lines:
    ass = Assignment(line)
    if ass.Is_coverring_at_all():
        sum+= 1

print(sum)
# The correct answet to the first part is 526
