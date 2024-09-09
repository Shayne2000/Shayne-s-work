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
bk.setup(width=160,height=160)

##### image ####

bk.bgpic(r"image\board.gif")
bk.register_shape(r"image\wp.gif")

#### list ####

white = []
balck = []

DOT = []

#### global variable #####

k = King(1,1,white,black,DOT,Object)

    
for i in range(8) :
    for n in range(8) :
        dot = Dot(DOT,i,n)
        dot.onclick(dot.click)
        


bk.mainloop()