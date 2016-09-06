from graphics import *
import math

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

dx=p2.getX()-p1.getX()
dy=p2.getY()-p1.getY()

dx2=p2.getX()-p3.getX()
dy2=p2.getY()-p3.getY()

dx3=p3.getX()-p1.getX()
dy3=p3.getY()-p1.getY()

s1=math.sqrt(dx**2+dy**2)
s2=math.sqrt(dx2**2+dy2**2)
s3=math.sqrt(dx3**2+dy3**2)

P=s1+s2+s3

s=(s1+s2+s3)/2

A=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print("Area: ",A," Perimeter: ",P)
