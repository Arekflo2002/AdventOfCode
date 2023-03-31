from collections import deque


class Point: 

    def __init__(self,x,y,value) -> None:
        self.row = x
        self.column = y
        self.value = value 
        self.explored = False
        self.parent = None


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

        if curr_point.value == 'S':
            curr_point.value = 'a'
        # Getting the points and checking that they arent beyond the lengths of the board
        if y-1 >= 0:
            ableToMoveThere.append(self.map.board[x][y-1])
        
        if y+1 < len(self.map.board[x]):
            ableToMoveThere.append(self.map.board[x][y+1])

        if x-1 >= 0:
            ableToMoveThere.append(self.map.board[x-1][y])
        
        if x +1 < len(self.map.board):
            ableToMoveThere.append(self.map.board[x+1][y])

        # I have Points where i Can technically move, but i dont know if I am able to, so i need to check that
        ableToMoveThereForSure = []
        for point in ableToMoveThere:
            if ord(point.value) == 1 + ord(curr_point.value) or ord(point.value) == ord(curr_point.value):
                ableToMoveThereForSure.append(point)
            
            elif curr_point.value == 'z' and point.value == 'E':
                ableToMoveThereForSure.append(point)

        return ableToMoveThereForSure


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
            # This is the points that i CAN and I AM AbLE TO move 
            pointsToMove = self.searching_pointsToMove(current_point)
            
            # So Im adding new points based on either they are explored or not
            for point in pointsToMove:
                if not point.explored:
                    point.explored = True
                    point.parent = current_point
                    queue.append(point)
        
        return current_point


    def counting_steps(self):
        goal_point = self.alghorithm_for_win()
        # So I have my goal that have a parent and so on ... so now i Will count steps and go backwords
        # Till I dont go back into my starting position 
        current_point = goal_point
        steps = 1
        while current_point.value != self.map.startingPoint.value:
            print(current_point.row,current_point.column,current_point.value)
            current_point = current_point.parent
            steps += 1

        return steps 
        

            




with open("Programy_adwentowe_2022\Zadanie12_Input.txt") as f:
    lines = f.readlines()

puzzle = Puzzle(lines)

print(puzzle.counting_steps())  
