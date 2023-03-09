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




class Tail(Point):

    def __init__(self):
        super().__init__(0,0)


class CoordinateSystem:

    def __init__(self):
        self.head = Head()
        self.tail = Tail()
        self.pointsOf_TailTravel = []
        self.pointsOf_TailTravel.append(Point(0,0))

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

    def tailMove_diagonally(self):
        # Moves for tail diagonally
        if self.head.x > self.tail.x and self.head.y > self.tail.y:
            self.tail.x += 1
            self.tail.y += 1

        elif self.head.x > self.tail.x and self.head.y < self.tail.y:
            self.tail.x += 1
            self.tail.y -= 1

        elif self.head.x < self.tail.x and self.head.y > self.tail.y:
            self.tail.x -= 1
            self.tail.y += 1

        elif self.head.x < self.tail.x and self.head.y < self.tail.y:
            self.tail.x -= 1
            self.tail.y -= 1


    def tailMove_normal(self):
        if self.head.x >self.tail.x:
            self.tail.x += 1


        elif self.head.x < self.tail.x:
            self.tail.x -= 1


        elif self.head.y > self.tail.y:
            self.tail.y += 1

        elif self.head.y<self.tail.y:
            self.tail.y -=1


    def tailToMove(self,distance):
        if distance < 2:
            # The points are "touching" so there is no need to move tail
            return

        elif distance == 2:
            # The points are apart but not diagonally, we need to check in what direction we need to go
            self.tailMove_normal()

        elif distance > 2:
            self.tailMove_diagonally()


        new_point = Point(self.tail.x,self.tail.y)
        # Just making sure that tail didnt travel multiple times in one point
        if new_point not in self.pointsOf_TailTravel:
            self.pointsOf_TailTravel.append(new_point)




    def mainMove(self,line):
        # So The first thing to do is get Data from line
        directon,valueOf_direction = self.gettingDataFromLine(line)
        valueOf_direction = int(valueOf_direction)

        # We need to move head as the input say !
        for move in range(valueOf_direction):
            # The next step is to let Head move
            self.headToMove(directon)
            # The next thing is to check the distance beetwen the points, so we can decide whether tail should move or not
            distance = math.sqrt(pow((self.head.y-self.tail.y),2)+pow((self.head.x-self.tail.x),2))
            self.tailToMove(distance)



    def answerToPuzzle_I(self):
        # todo: Can i Make this easier becouse its not elegenat
        # So this is the not elegant way:

        # unique_points = set()
        # unique_objects = []
        # for point in self.pointsOf_TailTravel:
        #     if (point.x, point.y) not in unique_points:
        #         unique_points.add((point.x, point.y))
        #         unique_objects.append(point)

        # This is the more elegant way to do wat it, but it needs the implrementation of eq and hash in Point class
        unique_objects = list(set(self.pointsOf_TailTravel))

        return len(unique_objects)


# Program


with open("Zadanie9_Input.txt") as f:
    lines = f.readlines()

cordinateSystem = CoordinateSystem()

for line in lines:
    cordinateSystem.mainMove(line)

print(cordinateSystem.answerToPuzzle_I())
