black = []
white = []
import turtle
from setup_piece import Chess_pieces

class Knight(Chess_pieces) :
    def __init__(self,x,y,z,r,dotList,list_object,turn):
        shape = [r"image\wh.gif",r"image\bh.gif"]
        Chess_pieces.__init__(self,x,y,z,r,dotList,list_object,turn,shape)
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList :
            if i == (x,y) :
                n = "none"
        for i in self.anotherColorList :
            if i == (x,y) :
                n = "take"
        if y <= 8 and y >= 1 and x <= 8 and x >= 1 and n == "move":
            if ((y == self.y+2 or y == self.y -2) and (x == self.x + 1 or x == self.x - 1)) or ((y== self.y +1 or y == self.y -1) and (x == self.x +2 or x == self.x -2)) :
                self.sameColorList.remove((self.x,self.y))
                self.sameColorList.append((x,y))
                self.x = x
                self.y = y
                print("you just move")
                self.goto(self.position())
            else :
                print("wierd")
        elif n == "take" :
            self.take(x,y)
        else :
            print(n)
    def take (self,x,y):
        for i in self.anotherColorList :
            #ถ้ามีอีกฝั่งอยู่
            if i == (x,y):
                #ถ้าเคลื่อนที่ถูกต้อง
                if y == self.y+2 or y == self.y -2:
                    if x == self.x + 1 or x == self.x - 1 :
                        for a in self.objectList :
                            if (a.x,a.y) == (x,y) :
                                print(a)
                                a.hideturtle()
                                print("already take")
                        self.sameColorList.remove((self.x,self.y))
                        self.anotherColorList.remove((x,y))
                        self.sameColorList.append((x,y))
                        self.x = x
                        self.y = y
                        print("yes you can")
                        self.goto(self.position())
                    else :
                        print("no you can't")
                elif y== self.y +1 or y == self.y -1:
                    if x == self.x +2 or x == self.x -2 :
                        for a in self.objectList :
                            if (a.x,a.y) == (x,y) :
                                print(a)
                                a.hideturtle()
                                print("already take")
                        self.sameColorList.remove((self.x,self.y))
                        self.anotherColorList.remove((x,y))
                        self.sameColorList.append((x,y))
                        self.x = x
                        self.y = y
                        print("yes you can")
                        self.goto(self.position())
                    else :
                        print("no you can't")
                else :
                    print("you can't do that")
    def showdot (self,x,y) :
        if self.turn[-1] == self.team :
            x = self.x
            y = self.y
            Directions = [(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2)]
            for i in self.dot_list :
                for n in Directions :
                    if (i.x,i.y) == n :
                        i.showturtle()
            self.status = 'true'
            #self.turn.append(self.turn[-2])
#a = bhorse(5,5)
#c = whorse(3,4)
#black.append((0,0))
#black.append(a.position())
#c.move(5,5)
#print(black)