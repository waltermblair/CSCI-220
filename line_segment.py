from graphics import *
import math

win=GraphWin(320,240)
win.setCoords(0,0,10,10)

Text(Point(5,9),"Click two points to make your line segment.").draw(win)

p1=win.getMouse()
p1.draw(win)

p2=win.getMouse()
p2.draw(win)

l=Line(p1,p2)
l.draw(win)

dx=p2.getX()-p1.getX()
dy=p2.getY()-p1.getY()

mid=Point(p2.getX()-dx/2,p2.getY()-dy/2)
mid.setFill("cyan")
mid.draw(win)

length=math.sqrt(dx**2+dy**2)
slope=dy/dx

print("Length: ",length,"\t Slope: ",slope)
