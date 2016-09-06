from graphics import *

def main():
    win=GraphWin()
    shape = Rectangle(Point(50,50),Point(75,75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p=win.getMouse()
        c=shape.getCenter()
        dx=p.getX()-c.getX()
        dy=p.getY()-c.getY()
        shape2=shape.clone()
        shape2.move(dx,dy)
        shape2.draw(win)
    win.close()
main()
