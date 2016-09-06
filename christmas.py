from graphics import *

win=GraphWin(300,300)
win.setCoords(0,0,100,100)

ground=Line(Point(0,5),Point(100,5))
ground.setWidth(5)
tree=Polygon(Point(10,5),Point(50,5),Point(30,80))
tree.setFill("green")
snow1=Circle(Point(75,15),10)
snow2=Circle(Point(75,30),5)

ground.draw(win)
tree.draw(win)
snow1.draw(win)
snow2.draw(win)

message=Text(Point(50,90),"Put a few ornaments on the tree!")
message.draw(win)
message.setFace("courier")

for i in range(5):
    p=win.getMouse()
    o=Circle(p,2)
    o.setFill("Red")
    o.setOutline("Red")
    o.draw(win)


