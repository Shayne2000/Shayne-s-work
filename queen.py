black = []
white = []
Directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
import turtle
from setup_piece import Chess_pieces

class Queen (Chess_pieces):
    def __init__(self,x,y,z,r,dotList,list_object,turn):
        shape = ["square",r"image\bq.gif"]
        Chess_pieces.__init__(self,x,y,z,r,dotList,list_object,turn,shape)
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList :
            if i == (x,y) :
                n = "none"
        for i in self.anotherColorList :
            if i == (x,y) :
                n = "take"
        if (self.x == x or self.y == y) and n == "move" :  #move like a rook
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.x = x
            self.y = y
            print("you just move")
            self.goto(self.position())
        elif x <= 8 and y <= 8 and x >= 1 and y >= 1 and ((self.x - x) == (self.y - y)or(self.x -x == -1*(self.y - y))) and n == 'move' :  #move like a bishop
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.x = x
            self.y = y
            print("you just move")
            self.goto(self.position())
        elif n == "take" :
            self.take(x,y)
            print("use function take")
        else :
            print(n)
    def take (self,x,y):
        for i in self.anotherColorList :
            #ถ้ามีอีกฝั่งใน position
            if i == (x,y):
                #check การเคลื่อนที่
                if self.x == x or self.y == y :
                    for a in self.objectList :
                        if (a.x,a.y) == (x,y) :
                            print(a)
                            a.hideturtle()
                            print("already take")
                    self.anotherColorList.remove((x,y))
                    self.sameColorList.remove((self.x,self.y))
                    self.sameColorList.append((x,y))
                    self.x = x
                    self.y = y
                    self.goto(self.position())
                elif x <= 8 and y <= 8 and x >= 1 and y >= 1 and ((self.x - x) == (self.y - y)or(self.x -x == -1*(self.y - y))) :
                    for a in self.objectList :
                            if (a.x,a.y) == (x,y) :
                                print(a)
                                a.hideturtle()
                                print("already take")
                    self.anotherColorList.remove((x,y))
                    self.sameColorList.remove((self.x,self.y))
                    self.sameColorList.append((x,y))
                    self.x = x
                    self.y = y
                    self.goto(self.position())
                else :
                    print("no you can't")
    def showdot (self,x,y) :
        if self.turn[-1] == self.team :
            global Directions
            for i in Directions :
                x = i[0]
                y = i[1]
                while  self.x + x <= 8 and self.y + y <= 8 and self.x + x >= 0 and self.y + y >= 0 :
                    for n in self.dot_list : 
                        if (self.x + x) == (n.x) :
                            if (self.y + y) == (n.y):
                                n.showturtle()
                                break
                    x = x + i[0]
                    y = y + i[1]
            self.status = 'true'
            #self.turn.append(self.turn[-2])
#q = Wqueen(0,0)
#print(white)