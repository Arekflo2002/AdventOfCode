from collections import deque

#Class


class Point:
    # So i need to make this class comparable so:
    def __eq__(self, other):
        # So i compare objects by x and y values !
        return self.row == other.row and self.column == other.column

    def __init__(self, x, y, value):
        self.row = x
        self.column = y
        self.value = value
        self.parent = None
        self. explored = False


class Plan:
    def __init__(self, lines):
        self.map = []
        self.startingPoint = None
        self.endPoint = None
        self.getting_data(lines)

    def getting_data(self, lines):
        # Yea my idea is to create 2 dimensional array and treat it as a map, and the 2 points I need to highlight
        # are the start and end points so i do this by char.isupper as the points are capitalized
        for line in lines:
            # we create list to contain current row
            curr_row = []
            for char in line:
                # So need to skip /n signs
                if char.isspace():
                    continue

                # we collect Points across the map, highlighting the start and the end point
                x = lines.index(line)
                y = line.index(char)
                if char.isupper():
                    if char == 'S':
                        self.startingPoint = Point(x, y, 'a')
                    elif char == 'E':
                        self.endPoint = Point(x, y, 'E')

                curr_row.append(Point(x,y,char))

            self.map.append(curr_row)


class System:

    def __init__(self, lines):
        # Getting my input map into the program
        self.plan = Plan(lines)

    def searchWhereToMove(self,point):

        # so I need to pick up the squares where i can acutally move
        avaible_roads = []
        for i_row in range(len(self.plan.map)):
            # So basically i go through all map and pick up the previous row and the next row of the Point
            if point.row - 1 == i_row  or point.row + 1 == i_row:
                x = i_row
                # The next step is to go through all that rows and find the points that are in the same columns as the Point, so that way
                # I will get Points that are below and up the Point
                for i_square in range(len(self.plan.map[i_row])):
                    if point.column == i_square :
                        y = i_square
                        avaible_roads.append(Point(x, y, self.plan.map[i_row][i_square].value))

            # So this if will grab the points that are next to(horizontally) to the Point
            elif point.row == i_row:
                x = i_row
                # So yea now i need to check if the column is behind or before starting point
                for i_square in range(len(self.plan.map[i_row])):
                    if point.column - 1 == i_square or point.column + 1 == i_square:
                        y = i_square
                        avaible_roads.append(Point(x,y,self.plan.map[i_row][i_square].value))

        # So now i have points that are avaible to move by their position and i select the points that I can actually move to that are higher than the
        #  point!:

        temp = []

        # So this is caused by for loop 'problems' by Python you cant remove items on the list that you are itering for
        for p in avaible_roads:
            if ord(p.value) - 1 == ord(p.value) or ord(p.value) == ord(point.value):
                temp.append(point)

        return temp


    def procedure(self):

        queue = deque()
        self.plan.startingPoint.explored = True
        queue.append(self.plan.startingPoint)
        steps = 1

        while len(queue)!= 0:
            print(1123)
            temp = queue

            for point in temp:
                legals_moves = self.searchWhereToMove(point)
                legals_moves_notExplored = list(filter(lambda x: x.explored == True,legals_moves))

                for point2 in legals_moves_notExplored:
                    point2.explored = True
                    # if p is not None :
                    #     point2.parent = p
                    queue.append(point2)

            p = queue.popleft()
            if p.value == 'E':
                return p


    def mainProgram(self):
        answer = self.procedure()
        print(answer.row,answer.column)


with open("Zadanie12_Input.txt") as f:
    lines = f.readlines()

system = System(lines)
system.mainProgram()
