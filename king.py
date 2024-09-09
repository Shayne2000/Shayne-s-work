from setup_piece import Chess_pieces


black = []
white = []

class King (Chess_pieces) :
    def __init__(self,x,y,z,r,D,list_object,turn):
        shape = "square"
        Chess_pieces.__init__(self,x,y,z,r,D,list_object,turn,shape)
    def move (self,x,y) :
        n = "move"
        for i in self.sameColorList :
            if i == (x,y) :
                n = "none"
        for i in self.anotherColorList :
            if i == (x,y) :
                n = "take"
        if y - self.y >= -1 and y-self.y <= 1 and x - self.x >= -1 and x - self.x <= 1 and n == "move" :
            self.sameColorList.remove((self.x,self.y))
            self.sameColorList.append((x,y))
            self.x = x
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
                if y - self.y >= -1 and y-self.y <= 1 and x - self.x >= -1 and x - self.x <= 1 :
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
        if self.turn[-1] == self.team :
            x = [-1,0,1]
            y = x[:]
            Directions = []
            for i in x :
                for q in y :
                    Directions.append((i,q))
            for i in Directions :
                for n in self.dot_list :
                    if (n.x,n.y) == (self.x+i[0],self.y+i[1]) :
                        n.showturtle()
            self.status = 'true'
            #self.turn.append(self.turn[-2])
    