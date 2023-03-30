from collections import deque


class Point: 

    def __init__(self,x,y,value) -> None:
        self.row = x
        self.column = y
        self.value = value 
        self.explored = False


class Map:

    def __init__(self,data) -> None:
        self.board = []
        self.startingPoint = None
        self.endingPoint = None
        self.getting_data(data)  

    def getting_data(self,data):
        
        # I will create a board, and make each Point for each letter in the map
        for i_row,row in enumerate(data):
            empty_row = []
            for j_letter,letter in enumerate(row):
                # Creating Point 
                point = Point(i_row,j_letter,letter)
                # As im creating the board, Im looking for starting/ending point
                if letter == 'S':
                    self.startingPoint = point
                elif letter == 'E':
                    self.endingPoint = point

                # Creating a row
                empty_row.append(point)
            
            # Creating a Board 
            self.board.append(empty_row)
    
    def printing(self):

        for row in self.board:
            for letter in row:
                if letter is not None:
                    print(letter.value,end="")
            print("")
                
class Puzzle: 
    # This is where i Will solve this puzzle 

    def __init__(self,data) -> None:
        self.map = Map(data)

    def searching_pointsToMove(self,curr_point):
        # I neeed to find points next to my curr_point and below and above it, then I will decide whether
        # I could move to that point
        ableToMoveThere = []
        x,y = curr_point.row,curr_point.column

        above = self.map.board[]
        
    
    def alghorithm_for_win(self):
        # I create a queue 
        queue = deque()
        
        queue.append(self.map.startingPoint)
        # Starting an algorithm
        while len(queue) != 0:
            # dequing a point from queue
            current_point = queue.popleft()
            
            # Checking whether the point is the goal 
            if current_point.value == 'E':
                return current_point
            






with open("Programy_adwentowe_2022\Test.txt") as f:
    lines = f.readlines()

map = Map(lines)

print(map.endingPoint.row)
