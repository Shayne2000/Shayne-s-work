import turtle 

black = []
white = []


class Chess_pieces (turtle.Turtle):
    def __init__(self,x,y,sameColorList,anotherColorList,dotList,objectList,turn,shape):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.up()
        self.x = x
        self.y = y
        self.sameColorList = sameColorList
        self.anotherColorList = anotherColorList
        self.goto(self.position())
        sameColorList.append((x,y))
        self.dot_list = dotList
        self.status = 'false'
        self.objectList = objectList
        objectList.append(self)
        self.turn = turn
        
        if self.y > 4 :
            self.team = "black"
            self.color("red")
        elif self.y < 5 :
            self.team = "white"
            self.color("blue")
            
            
        if type(shape) == str : 
            self.shape(shape)
        elif type(shape) == list :
            if self.team == "black" :
                self.shape(shape[1])
            elif self.team == "white" :
                self.shape(shape[0])
                
        self.onclick(lambda a,b : self.my_onclick(False,False))
    def my_onclick (self,x,y) :
        for i in self.dot_list :
            if i.isvisible() :
                i.hideturtle()
        self.showdot(self.x,self.y)
        
    def position (self):
        return (( -511+(self.x-1)*146 , -511+(self.y-1)*146 )) #(a+x,1+y)