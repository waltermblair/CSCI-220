from graphics import *

def drawWin():
    win=GraphWin(320,240)
    win.setCoords(0,0,100,100)
    shape=Circle(Point(50,50),25)
    shape.setFill('pink')
    shape.draw(win)
    Text(Point(50,90),"Click anywhere to move the circle").draw(win)
    return win, shape

def moveTo(shape, newCenter):
    center=shape.getCenter()
    dx=newCenter.getX()-center.getX()
    dy=newCenter.getY()-center.getY()
    shape.move(dx,dy)

def main():
    win, shape = drawWin()
    for i in range(10):
        newCenter=win.getMouse()
        moveTo(shape, newCenter)

main()
