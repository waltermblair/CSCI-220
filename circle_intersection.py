import math
from graphics import *

print("This program computes the two points where your horizontal line intersects with my circle.")

r=eval(input("The radius of the circle: "))
y=eval(input("The y-intercept of the line: "))

try:
    x1=math.sqrt(r**2-y**2)
    x2=-x1

    print("Points of intersect: (",x1,y,") and (",x2,y,")")
    print("Thank you, come again.")

    win=GraphWin()
    win.setCoords(-12,-12,12,12)
    xaxis=Line(Point(-12,0),Point(12,0))
    yaxis=Line(Point(0,-12),Point(0,12))
    xaxis.draw(win)
    yaxis.draw(win)

    for i in range(0,22,2):
        Text(Point(-10+i+0.5,-.5),-10+i).draw(win)
        Text(Point(-.5,-10+i+0.5),-10+i).draw(win)

    c=Circle(Point(0,0),r)
    c.draw(win)
    l=Line(Point(-12,y),Point(12,y))
    l.setWidth(2)
    l.draw(win)

    p1=Point(x1,y)
    p1.setFill("red")
    p1.draw(win)
    p2=Point(x2,y)
    p2.setFill("red")
    p2.draw(win)

except:
    print("The line does not intersect!")
