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
        self.whereToMove = []
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



    def whereSquaresGo(self):

        queue = deque()
        self.startingPoint.explored = True
        queue.append(self.startingPoint)
        steps = 1
        while len(queue) != 0 :
            v = queue.popleft()

            if v.value != 'E':
                return steps

            for point in queue:
                legals_moves = 123









class SearchShortestPath:

    def __init__(self):
        self.goal = None


    def procedure(self,graph,root):

        # label root as explored
        qraph = deque()
        qraph.append(root)

        while len(qraph) != 0:
            v = qraph.popleft()

            if v == self.goal:
                return v





