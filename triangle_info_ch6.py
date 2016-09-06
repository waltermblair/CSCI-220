from graphics import *
import math

def square(x):
    return x*x

def distance(p1,p2):
    dist=math.sqrt(square(p2.getX()-p1.getX())
                   +square(p2.getY()-p1.getY()))
    return dist

def area(s1,s2,s3, window):
    s=(s1+s2+s3)/2
    A=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    Text(Point(5,8),"Area: {0:0.2f}".format(A)).draw(window)
    return A

def main():
    win=GraphWin(320,240)
    win.setCoords(0,0,10,10)

    Text(Point(5,9),"Click three points of your triangle").draw(win)

    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)

    poly=Polygon(p1,p2,p3)
    poly.draw(win)

    s1=distance(p1,p2)
    s2=distance(p2,p3)
    s3=distance(p1,p3)

    P=s1+s2+s3
    A=area(s1,s2,s3, win)
    
    print("Area: ",A," Perimeter: ",P)

main()
