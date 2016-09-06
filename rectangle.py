from graphics import *
import math

win=GraphWin(320,240)
win.setCoords(0,0,10,10)

Text(Point(5,9),"Click two opposite corners of your rectangle").draw(win)

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

dx=p2.getX()-p1.getX()
dy=p2.getY()-p1.getY()

p3=Point(p1.getX(),p1.getY()+dy)
p4=Point(p1.getX()+dx,p1.getY())
p3.draw(win)
p4.draw(win)

poly=Polygon(p1,p3,p2,p4)
poly.draw(win)

dx2=p2.getX()-p3.getX()
dy2=p2.getY()-p3.getY()

dx3=p2.getX()-p4.getX()
dy3=p2.getY()-p4.getY()

l=math.sqrt(dx2**2+dy2**2)
w=math.sqrt(dx3**2+dy3**2)

P=2*l+2*w
A=l*w

print("Area: ",A," Perimeter: ",P)
