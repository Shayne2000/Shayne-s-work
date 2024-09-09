import turtle
from setup_piece import Chess_pieces


black = []
white = []

class Wpawn (Chess_pieces) :
    def __init__(self,x,y,sameColorList,anotherColorList,dotList,list_object,turn):
        shape = r"image\wpresize.gif"
        Chess_pieces.__init__(self,x,y,sameColorList,anotherColorList,dotList,list_object,turn,shape)
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList :
            if i == (x,y) :
                n = "none"
        for i in self.anotherColorList :
            if i == (x,y) :
                n = "take"
        if y == self.y+1 and x == self.x and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.y = y
            print("you just move")
            self.goto(self.position())
        elif self.x == x and self.y == 2 and y == 4 and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.y = y
            print("you just move")
            self.goto(self.position())
        elif n == "take" :
            self.take(x,y)
        else :
            print(n)
    def take (self,x,y):
        for i in self.anotherColorList :
            #ถ้ามีอีกฝั่งใน position
            if i == (x,y):
                #check การเคลื่อนที่
                if ((x,y) == (self.x+1,self.y+1) or (x,y) == (self.x-1,self.y+1)) and x >= 1 and x <= 8 and y <= 8:
                    for a in self.objectList :
                        if (a.x,a.y) == (x,y) :
                            print(a)
                            a.hideturtle()
                            print("take")
                        else :
                            print("can't take")
                    print("yes you can")
                    self.anotherColorList.remove((x,y))
                    self.sameColorList.remove((self.x,self.y))
                    self.x = x
                    self.y = y
                    self.sameColorList.append((x,y))
                    self.goto(self.position())
                else :
                    print("no you can't")
    def showdot (self,x,y) :
        if self.turn[-1] == "white" :
            Directions = [(self.x,self.y+1),(self.x-1,self.y+1),(self.x+1,self.y+1),(self.x,self.y+2)]
            for i in Directions :
                for n in self.dot_list :
                    if (n.x,n.y) == i :
                        n.showturtle()
            self.status = 'true'
            #self.turn.append(self.turn[-2])
    
    
############################################################################################################################################
#####################################################################################################################################################
##################################################################################################################################
    
    
class Bpawn(Chess_pieces) :
    def __init__(self,x,y,z,r,D,list_object,turn):
        shape = r"image\bp(1).gif"
        Chess_pieces.__init__(self,x,y,z,r,D,list_object,turn,shape)
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList :
            if i == (x,y) :
                n = "none"
        for i in self.anotherColorList :
            if i == (x,y) :
                self.take(x,y)
        if y == self.y-1 and x == self.x and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.y = y
            print("yes you can")
            self.goto(self.position())
        elif self.x == x and self.y == 7 and y == 5 and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.y = y
            print("yes you can")
            self.goto(self.position())
    def take (self,x,y):
        for i in self.anotherColorList :
            if i == (x,y):
                if (x,y) == (self.x+1,self.y-1) or (x,y) == (self.x-1,self.y-1) and x >= 1 and x<=8 and y >= 1:
                    print("yes you can")
                    for a in self.objectList :
                        if (a.x,a.y) == (x,y) :
                            print(a)
                            a.hideturtle()
                            print("take")
                        else :
                            print("can't take")
                    self.anotherColorList.remove((x,y))
                    self.sameColorList.remove((self.x,self.y))
                    self.x = x
                    self.y = y
                    self.sameColorList.append((x,y))
                    self.goto(self.position())
                else :
                    print("no you can't")
            else :
                print("no you can't")
    def showdot (self,x,y) :
        print("\nbefore : ",self.turn)
        print("last object in this list : ",self.turn[-1])
        if self.turn[-1] == "black" :
            Directions = [(self.x,self.y-1),(self.x-1,self.y-1),(self.x+1,self.y-1),(self.x,self.y-2)]
            for i in Directions :
                for n in self.dot_list :
                    if (n.x,n.y) == i :
                        n.showturtle()
            self.status = "true"
            #self.turn.append("white")
            print("after : ",self.turn)
    