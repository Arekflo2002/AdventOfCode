# Classes

# For I part

class Tree:

    def __init__(self,height):
        self.height = height
        self.isVisible = False
        self.scenicScore = 0


class Grid:

    def __init__(self):
        self.grid = []
        self.sumof_visible = 0

    #region I Part
    def filling_grid(self,lines):

        for line in lines:
            row = []
            for char in line:
                if not char.isspace():
                    temp = Tree(int(char))
                    row.append(temp)

            self.grid.append(row)

    def outerTreesTidies(self):
        # So the idea behind this function is to make all outer trees Visible becouse thats the assumptions
        for i_row in range(len(self.grid)):
            # So for starters I start with top and botoom
            if i_row == 0 or i_row==len(self.grid)-1:
                for i_tree in range(len(self.grid[i_row])):
                    self.grid[i_row][i_tree].isVisible = True

        # The next step are the flanks
        for i_row in range(len(self.grid)):
            if i_row != 0 and i_row != len(self.grid)-1:
                for i_tree in range(len(self.grid[i_row])):
                    if i_tree == 0 or i_tree == len(self.grid[i_row])-1:
                        self.grid[i_row][i_tree].isVisible = True


    def finding_row(self,index_row,index_col):
        # This function seeks for
        row_before = []
        row_after = []
        for i_tree in range(len(self.grid[index_row])):
            if i_tree == index_col:
                continue
            elif i_tree < index_col:
                row_before.append(self.grid[index_row][i_tree].height)
            else:
                row_after.append(self.grid[index_row][i_tree].height)

        return row_before,row_after

    def finding_column(self,index_row,index_col):
        column_before = []
        column_after = []

        for i_row in range(len(self.grid)):
            for i_tree in range(len(self.grid[i_row])):
                if i_tree == index_col:
                    if i_row < index_row:
                        column_before.append(self.grid[i_row][i_tree].height)
                    if i_row > index_row:
                        column_after.append(self.grid[i_row][i_tree].height)
                    else:
                        continue

        return column_before,column_after

    def isVisible_FromThisSide(self,listof,height):
        # So I pass the side(top/bottom etc... ) and function tells me whether the three is Visible from that side
        listof.append(height)
        maxim = max(listof)
        if height == maxim:
            if listof.count(maxim) > 1:
                return False
            else:
                return True
        else:
            return False

    def __puzzle_Part_1(self):
        # First I take care of the outer trees
        self.outerTreesTidies()

        # So this function goes after all trees and "look" at the grid from bottom/top/right/left and check if the three is visible or not
        for i_row in range(len(self.grid)):
            for i_tree in range(len(self.grid[i_row])):
                row_before,row_after = self.finding_row(i_row, i_tree)
                column_before,column_after = self.finding_column(i_row, i_tree)
                current_tree = self.grid[i_row][i_tree]
                # So I Check if three is visible from at least one side
                if (
                        self.isVisible_FromThisSide(row_before,current_tree.height) or
                        self.isVisible_FromThisSide(row_after,current_tree.height) or
                        self.isVisible_FromThisSide(column_before,current_tree.height) or
                        self.isVisible_FromThisSide(column_after,current_tree.height)
                    ):
                    self.grid[i_row][i_tree].isVisible = True
                else:
                    self.grid[i_row][i_tree].isVisible = False


    def answer_to_puzzlePart_1(self):
        self.__puzzle_Part_1()
        sum = 0
        for row in self.grid:
            for tree in row:
                if tree.isVisible:
                    sum += 1
        self.sumof_visible = sum
        return sum

    #endregion I Part

    #region II Part
    def __calculating_distance_side(self, listof, current_tree):
        sum = 0
        for height in listof:
            if current_tree.height <= height:
                sum += 1
                break
            elif current_tree.height > height:
                sum += 1
        return sum

    def __calculating_distance(self, rowb, rowa, colb, cola, current_tree):
        # So basically i Check how much distance is beetwen THE tree and the three that is higher or the edge, Then i will multiplay the results
        right = self.__calculating_distance_side(rowa, current_tree)
        left = self.__calculating_distance_side(rowb, current_tree)
        top = self.__calculating_distance_side(colb, current_tree)
        bottom = self.__calculating_distance_side(cola, current_tree)

        return right * left * top * bottom

    def __puzzle_Part_II(self):
        for i_row in range(len(self.grid)):
            for i_tree in range(len(self.grid[i_row])):
                current_tree = self.grid[i_row][i_tree]
                # It pointless to even consider trees that are Visible bcs elves dont want them
                if 1:
                    row_before, row_after = self.finding_row(i_row, i_tree)
                    column_before, column_after = self.finding_column(i_row, i_tree)
                    # So there is need to reverse that becouse i gather this using for loop and before the moment Where THE tree stands
                    # my list seems is reversed becouse i iterate from 0 but the I start from the furtherst distance so one of this
                    # variable must be reversed
                    row_before.reverse()
                    column_before.reverse()
                    # So im calculating the Scenic Score
                    current_tree.scenicScore = self.__calculating_distance(row_before, row_after, column_before,column_after,current_tree)


    def answer_to_puzzlePart_2(self):
        self.__puzzle_Part_II()
        listof_maxim = []
        maxim = 0
        for row in self.grid:
            temp_max = max(row, key=lambda x: x.scenicScore,default=0)
            if temp_max != 0:
                listof_maxim.append(temp_max)

        maxim = max(listof_maxim, key=lambda x: x.scenicScore).scenicScore
        return maxim
    #endregion II Part

    def out(self):
        for row in self.grid:
            for tree in row:
                print(tree.scenicScore,end=" ")
            print("\n")



with open("Zadanie8_Input.txt") as f :
    lines = f.readlines()

# This is the solution to the first part
grid = Grid()
grid.filling_grid(lines)
print("I part:" + str(grid.answer_to_puzzlePart_1()))

# This is the solution to the second part

print("II Part: "+str(grid.answer_to_puzzlePart_2()))

