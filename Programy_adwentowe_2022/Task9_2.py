import math


# Classes
class Point:
    # So Im trying to make my point unique so later in program i can easily detech which points repeated
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(('x',self.x,'y',self.y))

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        string = str(self.x) +':'+str(self.y)
        return string


class Head(Point):

    def __init__(self):
        super().__init__(0,0)

class Knot(Point):
    def __init__(self,name):
        super().__init__(0,0)
        self.name = str(name)
        self.isCovered = True
        self.travel_points = []
        self.travel_points.append(Point(0, 0))

    def addingTravel(self, point):
        self.travel_points.append(point)

    def distanceTravelled(self):
        return len(self.travel_points)


class Rope:

    def __init__(self):
        self.knots = []
        self.fillingRope()

    def fillingRope(self):
        for i in range(9):
            temp = Knot(i+1)
            self.knots.append(temp)

    def out(self):
        str =""
        for i in self.knots:
            str += i.name
        return str

class CoordinateSystem:

    def __init__(self):
        self.head = Head()
        self.rope = Rope()

    def gettingDataFromLine(self,line):
        # So the function get me the variables from the line
        direction = ""
        value =""
        for char in line:

            if not char.isspace() and not char.isdigit():
                direction += char

            elif not char.isspace() and char.isdigit():
                value += char

        return direction, value

    def headToMove(self,direction):
        # Just reading the input
        if direction.upper() == 'U':
            self.head.y += 1

        elif direction.upper() == 'D':
            self.head.y -= 1

        elif direction.upper() == 'R':
            self.head.x += 1

        elif direction.upper() == 'L':
            self.head.x -= 1

    def knotMove_diagonally(self,knot1,knot2):
        if knot1.x > knot2.x and knot1.y > knot2.y:
            knot2.x += 1
            knot2.y += 1

        elif  knot1.x > knot2.x and knot1.y < knot2.y:
            knot2.x += 1
            knot2.y -= 1

        elif  knot1.x < knot2.x and knot1.y > knot2.y:
            knot2.x -= 1
            knot2.y += 1

        elif  knot1.x < knot2.x and knot1.y < knot2.y:
            knot2.x -= 1
            knot2.y -= 1

    def knotMove_normal(self,knot1,knot2):
        if knot1.x > knot2.x:
            knot2.x += 1
        elif knot1.x < knot2.x:
            knot2.x -= 1
        elif knot1.y > knot2.y:
            knot2.y += 1
        elif knot1.y < knot2.y:
            knot2.y -= 1

    def knotToMove(self,knot1,knot2):
        # So this function I calculate distance beetwen knot and Head
        distance = self.calculating_distance(knot1,knot2)

        if distance < 2:
            pass
        if distance == 2:
            self.knotMove_normal(knot1,knot2)
        else:
            self.knotMove_diagonally(knot1,knot2)

    def calculating_distance(self, knot1,knot2):
        # So the function calculates distance beetwen 2 objects
        distance = math.sqrt(pow((knot1.y - knot2.y), 2) + pow((knot1.x - knot2.x), 2))
        return distance

    def moveAtAll_rope(self, knot1,knot2):
        distance =  self.calculating_distance(knot1,knot2)
        if distance < 2:
            # The points are touching each other so there is no need to move them
            return False
        else:
            return True

    def isKnotCovered(self,index):
        # So this function basically tries to figures if the knot is covered and if it should move

        # So This loop check for knot being covered in reversed order, if the head or any higher knot cover this particular knot
        # I set its parameter isCovered to True, otherwise I set it to True
        current_knot = self.rope.knots[index]

        if current_knot == self.head:
            return True
        else:
            for knot in reversed(self.rope.knots):
                if knot.x == current_knot.x and knot.y == current_knot.y:
                    return False
                else:
                    if knot == current_knot:
                        return True


    def ropeToMove(self):
        # So, my approach will be to check distance beetwen first knot and the head, and decide if the rope need to move at all
        # I use double negation becouse to make it easier

        if not self.moveAtAll_rope(self.head,self.rope.knots[0]):
            return

        # We need to move the rope
        else:
            for i_knot in range(len(self.rope.knots)):
                # So first i gotta know if the knot is covered(the term is explained in the function), double negation to make it easier
                if not self.isKnotCovered(i_knot):
                    # We give a special treamnet for first knot becouse it must follows the head, so it wont play by the same rules as
                    # the next knots
                    if i_knot == 0:
                        self.knotToMove(self.head,self.rope.knots[i_knot])
                    # Then we begin fun with the rest of the knots
                    else:

                        # We need to check if there is need to move them, we will check this by checking if they "touch" previous knot
                        if self.moveAtAll_rope(self.rope.knots[i_knot-1],self.rope.knots[i_knot]):
                            self.knotToMove(self.rope.knots[i_knot-1],self.rope.knots[i_knot])
                            # There is gathering data for our solution, we gather the point that our knot just moved in
                            # and we hope that its the tail
                            current_knot = self.rope.knots[i_knot]
                            current_knot.addingTravel(Point(current_knot.x,current_knot.y))


    def mainMove(self,line):
        # So the first fight is to gather data where head is headed to ;)
        direction, valueof_direction = self.gettingDataFromLine(line)

        for move in range(int(valueof_direction)):
            # So now we make x moves in direction pointed by data
            # First we move the head
            self.headToMove(direction)
            # The next thing would be to whole rope to move, thats where the most of the program will play out so
            self.ropeToMove()

    def answerToPuzzle_I(self):
        # So we need to get rid of the repeated points !!!

        unique_object = set(self.rope.knots[8].travel_points)
        result = len(unique_object)

        return result




# Program


with open("Zadanie9_Input.txt") as f:
    lines = f.readlines()

cordinateSystem = CoordinateSystem()

for line in lines:
    cordinateSystem.mainMove(line)



print("Result: "+str(cordinateSystem.answerToPuzzle_I()))  # 2477 Too high
