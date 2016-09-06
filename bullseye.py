from graphics import *

def drawTarget():
    win=GraphWin(320,240)
    win.setCoords(0,0,200,200)
    center=Point(100,100)
    white=Circle(center,100)
    white.setFill("white")
    black=Circle(center,80)
    black.setFill("black")
    blue=Circle(center,60)
    blue.setFill("blue")
    blue.setOutline("blue")
    red=Circle(center,40)
    red.setFill("red")
    red.setOutline("red")
    yellow=Circle(center,20)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)
    Text(Point(100,190), "Take five shots at the bullseye").draw(win)
    return win

def main():
    win=drawTarget()
    score=0
    for i in range(5):
        p=win.getMouse()
        p.draw(win)
        if p.getY()<=120 and p.getY()>=80 and p.getX()<=120 and p.getX()>=80:
            score=score+9
        elif p.getY()<=140 and p.getY()>=60 and p.getX()<=140 and p.getX()>=60:
            score=score+7
        elif p.getY()<=160 and p.getY()>=40 and p.getX()<=160 and p.getX()>=40:
            score=score+5
        elif p.getY()<=180 and p.getY()>=20 and p.getX()<=180 and p.getX()>=20:
            score=score+3
        elif p.getY()<=200 and p.getY()>=0 and p.getX()<=200 and p.getX()>=0:
            score=score+1
    print(score)
main()
