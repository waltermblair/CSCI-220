from graphics import *
from time import sleep

def drawWindow():
    win=GraphWin(320,240)
    win.setCoords(0,0,100,100)
    Text(Point(50,90),"Click to place the circle of doom").draw(win)
    c=win.getMouse()
    circ=Circle(c,20)
    circ.setFill('pink')
    circ.draw(win)
    return circ

def main():
    circ=drawWindow()
    dx=1
    dy=1
    for i in range(1000):
        center=circ.getCenter()
        x=center.getX()
        y=center.getY()
        
        if x>0:
            if x<100:
                dx=dx
            else:
                dx=-dx
        else:
            dx=-dx
        if y>0:
            if y<100:
                dy=dy
            else:
                dy=-dy
        else:
            dy=-dy

        circ.move(dx,dy)
            
        sleep(0.0005)
main()
