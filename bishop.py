black = []
white = []
objectList = []
Directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
from setup_piece import Chess_pieces
import turtle
piece_name = turtle.Turtle

class Bishop(Chess_pieces) :
    def __init__(self,x,y,z,r,dotList,objectList,turn):
        shape = ["square",r"image\bb.gif"]
        Chess_pieces.__init__(self,x,y,z,r,dotList,objectList,turn,shape)
        self.status = 'none'
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList : #same position as friends
            if i == (x,y) :
                n = "no"
        for i in self.anotherColorList : #same position as enamy
            if i == (x,y) :
                n = "take"
        if x <= 8 and y <= 8 and x >= 1 and y >= 1 and ((self.x - x) == (self.y - y) or (self.y - y)* -1 == self.x-x) and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.x = x
            self.y = y
            self.sameColorList.append((self.x,self.y))
            self.goto(self.position())
        elif n == "take" :
            self.take(x,y)
    def take (self,x,y):
        for i in self.anotherColorList : 
            #ถ้ามีอีกฝั่งใน position
            if i == (x,y):
                #check การเคลื่อนที่
                if (self.x - x) == (self.y - y) or (self.y - y)*-1 == self.x - x :
                    for a in self.objectList :
                        if (a.x,a.y) == (x,y) :
                            print(a)
                            a.hideturtle()
                    self.anotherColorList.remove((x,y))
                    self.sameColorList.remove((self.x,self.y))
                    self.x = x
                    self.y = y
                    self.sameColorList.append((x,y))
                    self.goto(self.position())
    def showdot (self,x,y) :
        print(self.team,"and",self.turn[-1])
        if self.team == self.turn[-1] :
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
            