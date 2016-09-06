#faceTime.py

from face import Face
from graphics import *
from button import *
from time import *

def drawWin():
    win=GraphWin()
    win.setCoords(0,0,100,100)
    center=Point(50,50)
    return win, center
    
def bounce(win, obj):
    dx=1
    dy=1
    while True:
        center=obj.getCenter()
        x=center.getX()
        y=center.getY()
        if x>0:
            if x<100:
                dx=dx
            else:
                dx=-dx
                obj.doWink(win)
        else:
            dx=-dx
            obj.doSmile(win)
        if y>0:
            if y<100:
                dy=dy
            else:
                dy=-dy
                obj.doWink(win)
        else:
            dy=-dy
            obj.doSurprise(win)
        obj.move(dx,2*dy) 
        sleep(0.00002)

def main():
    win,center=drawWin()
    myFace=Face(win, center, 20)
    bounce(win, myFace)
    
if __name__=="__main__": main()
