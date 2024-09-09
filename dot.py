import turtle as T

class Dot (T.Turtle) :
    def __init__(self,dotList,x,y) :
        T.Turtle.__init__(self)
    #### summoning jutsu ####
        self.speed(0)
        self.shape("circle")
        self.color("gray")
        self.hideturtle()
        self.up()
        self.x = x + 1
        self.y = y + 1
        self.goto((-511+(self.x-1)*146,-511+(self.y-1)*146))
        dotList.append(self)
        self.boo = "false"
        #self.onclick(self.click)
    def click (self,x,y):
        self.boo = "true"