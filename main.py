#### import class #####
from pawn import *
from horse import *
from rook import *
from bishop import *
from queen import *
from king import *

import turtle as T

from dot import Dot
##### screen ######

bk = T.Screen()
bk.setup(width=1200,height=1200)

##### image ####

#shape = ((20,20),(20,-20),(-20,-20),(-20,20))

bk.bgpic(r"image\greenone.png") #board
bk.register_shape(r"image\wpresize.gif") #white pawn
bk.register_shape(r"image\bp(1).gif") #black pawn
bk.register_shape(r"image\bh.gif") #black knight
bk.register_shape(r"image\wh.gif") #white knight
bk.register_shape(r"image\bb.gif") #black bishop
bk.register_shape(r"image\bq.gif") #black queen

#### list ####

white = []
balck = []

dotList = []

Object = []

#### global variable #####

turn = ["white","black","white"]


##### function ######

 


    
#### create white pawn ###

for i in range(8):
    wp = Wpawn(i+1,2,white,black,dotList,Object,turn)

#### create black pawn ####

for i in range(8):
    bp = Bpawn(i+1,7,black,white,dotList,Object,turn)
    
#### create white rook ###

wr1 = Rook(1,1,white,black,dotList,Object,turn)
wr2 = Rook(8,1,white,balck,dotList,Object,turn)

##### create black rook #### 

br1 = Rook(1,8,black,white,dotList,Object,turn)
br2 = Rook(8,8,black,white,dotList,Object,turn)

#### create white horse ####

wh1 = Knight(2,1,white,black,dotList,Object,turn)
wh2 = Knight(7,1,white,balck,dotList,Object,turn)

### create black horse ####

bh1 = Knight(2,8,black,white,dotList,Object,turn)
bh2 = Knight(7,8,black,white,dotList,Object,turn)

#####create bishop #####

wb1 = Bishop(3,1,white,black,dotList,Object,turn)
wb2 = Bishop(6,1,white,black,dotList,Object,turn)

bb1 = Bishop(3,8,black,white,dotList,Object,turn)
bb2 = Bishop(6,8,black,white,dotList,Object,turn)

#### create queen ####

wq = Queen(4,1,white,black,dotList,Object,turn)

bq = Queen(4,8,black,white,dotList,Object,turn)

#############create king#################

wk = King(5,1,white,black,dotList,Object,turn)

Bk = King(5,8,black,white,dotList,Object,turn)

## set color ########


#for i in white :
#    if i == 

##### main program #####

for i in range(8) :
    for n in range(8) :
        dot = Dot(dotList,i,n)
        

for i in dotList :
    i.onclick(i.click)



while True :
    for i in dotList :
        if i.boo == "true" :
            for a in Object : #test 1234
                if a.status == 'true' :
                    (x,y) = (a.position())
                    #print((x,y))
                    a.move(i.x,i.y)
                    #print(a.position())
                    if a.position() != (x,y) :
                        a.status = 'false'
                        i.boo = 'false'
                        a.turn.append(a.turn[-2])
                    else :
                        i.boo = "false"
                        a.status = "false"
                    for i in dotList :
                        i.hideturtle()
    bk.update()



#bk.mainloop()