
# Class

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

class Directory:

    def __init__(self,name,outer_dir):
        self.name = name
        self.listof_files = []
        self.listof_directories = []
        self.size = self.calculating_sizeofdir()
        self.outer_dir = outer_dir

    def calculating_sizeofdir(self):
        sum = 0
        if len(self.listof_directories) > 0:
            for dir in self.listof_directories:
                sum += dir.size
        sum += self.sum_of_files()
        return sum

    def moveInDirectory(self,name):
        return list(filter(lambda dire: dire.name == name, self.listof_directories))[0]

    def moveOutDirectory(self):
        return self.outer_dir

    def adding_directory(self,dir):
        self.listof_directories.append(dir)

    def adding_file(self,file):
        self.listof_files.append(file)
        self.size = self.calculating_sizeofdir()

    def sum_of_files(self):
        sum = 0
        for file in self.listof_files:
            sum+= file.size
        return sum



class DataBase:

    def __init__(self):
        self.mainDirectory = Directory('/',None)
        self.directories = []
        self.directories.append(self.mainDirectory)
        self.currentDirectory = self.mainDirectory

    def adding_directory(self,name):
        temp = Directory(name,self.currentDirectory)
        if temp not in self.directories:
            self.directories.append(temp)
            self.currentDirectory.adding_directory(temp)

    def refresh_size(self):
        for dir in reversed(self.directories):
            dir.size = dir.calculating_sizeofdir()

    def solving_puzzle_I(self):
        sum = 0

        for dir in self.directories:
            if dir.size <= 100000:
                sum += dir.size
        return sum

    def solving_puzzle_II(self):
        unused_space = 70000000 - self.mainDirectory.size
        needed_space = 30000000
        list_of_free_space = []
        for dir in self.directories:
            # So We check if deleting the directory will increse the unused space enough
            if unused_space + dir.size >= needed_space:
                list_of_free_space.append(dir.size)

        answer = min(list_of_free_space)
        return answer




    def out(self):
        str = ""
        for i in self.directories:
            str+=i.name
        return str


def gettingName(string):
    # So basically I go from behind untill I meet a space then I stop
    string = string[:len(string)-1]
    string_reversed = string[::-1]
    name = ""
    for char in string_reversed:
        if char.isspace():
            break
        name += char

    name = name[::-1]
    return str(name)


def gettingSize(string):
    size = ""

    for char in string:
        if char.isspace():
            break
        size+= char

    return int(size)




# Data

with open("Zadanie7_Input.txt") as f:
    lines = f.readlines()

# todo: Program

dtBase = DataBase()

for line in lines:
    # This is types of operations that can go in 1 line
    if '$' in line:
        # This means we will see ls or cd
        if "cd" in line:
            # What will happen if the operations is to change directories
            if "/" in line:
                # We need to know if the main directory was created
                dtBase.currentDirectory = dtBase.mainDirectory

            elif ".." in line:
                # What if we need to move out of the current directory
                dtBase.currentDirectory = dtBase.currentDirectory.moveOutDirectory()

            else:
                #What if we have to move in directory
                dtBase.currentDirectory = dtBase.currentDirectory.moveInDirectory(gettingName(line))

    # What will happen after the ls operation
    elif "dir" in line:
        # Basically adding a directory
        dtBase.adding_directory(gettingName(line))

    elif "dir" not in line and '$' not in line:
        # Basically adding files
        temp = File(gettingName(line),gettingSize(line))
        dtBase.currentDirectory.adding_file(temp)

dtBase.refresh_size()
print("I Part: "+str(dtBase.solving_puzzle_I())) # The right anwser is 1297159
print("II Part: "+str(dtBase.solving_puzzle_II()))