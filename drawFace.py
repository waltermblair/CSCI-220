from graphics import *

print("This program draws some faces")

def drawWindow():
    win=GraphWin(320,240)
    win.setCoords(0,0,100,100)
    Text(Point(50,90),"Click a few spots to draw faces").draw(win)
    return win

def drawFace(center, size, win):
    circ=Circle(center, size/2)
    mouth=Oval(Point(center.getX()-size/4,center.getY()-size/3),
               Point(center.getX()+size/4,center.getY()-size/4))
    nose=Polygon(center, Point(center.getX()-size/8,center.getY()-size/5),
                 Point(center.getX()+size/8,center.getY()-size/5))
    leye=Circle(Point(center.getX()-size/4,center.getY()+size/4),size/8)
    reye=leye.clone()
    reye.move(size/2,0)
    circ.draw(win)
    mouth.draw(win)
    nose.draw(win)
    leye.draw(win)
    reye.draw(win)


def main():
    win=drawWindow()
    center=win.getMouse()
    drawFace(center, 25, win)
    center=win.getMouse()
    drawFace(center, 40, win)
    center=win.getMouse()
    drawFace(center, 60, win)
main()
    
