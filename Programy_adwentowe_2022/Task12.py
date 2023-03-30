
class Point: 

    def __init__(self,x,y,value) -> None:
        self.row = x
        self.column = y
        self.value = value 


class Map:

    def __init__(self,data) -> None:
        self.board = []
        self.startingPoint = None
        self.getting_data(data)  

    def getting_data(self,data):
        
        # I will create a board, and make each Point for each letter in the map
        for i_row,row in enumerate(data):
            empty_row = []
            for j_letter,letter in enumerate(row):
                # Creating Point 
                point = Point(i_row,j_letter,letter)
                # As im creating the points/board, Im looking for starting/ending point
                if letter == 'S':
                    self.startingPoint = Point()
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
    





with open("Programy_adwentowe_2022\Test.txt") as f:
    lines = f.readlines()

map = Map(lines)

map.printing()
