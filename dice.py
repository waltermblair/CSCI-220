from graphics import *

win=GraphWin()
win.setCoords(0,0,100,100)

d=Rectangle(Point(10,50),Point(20,60))
d.setWidth(3)
n=Circle(Point(15,55),1)
n.setFill("black")

d1=d.clone()
n.draw(win)

d2=d.clone()
d2.move(15,0)
n2a=n.clone()
n2a.move(17.5,2.5)
n2b=n.clone()
n2b.move(12.5,-2.5)
n2a.draw(win)
n2b.draw(win)

d3=d.clone()
d3.move(30,0)
n3a=n.clone()
n3a.move(30,0)
n3b=n2a.clone()
n3b.move(15,0)
n3c=n2b.clone()
n3c.move(15,0)
n3a.draw(win)
n3b.draw(win)
n3c.draw(win)

d4=d.clone()
d4.move(45,0)
n4a=n3b.clone()
n4a.move(15,0)
n4b=n3c.clone()
n4b.move(15,0)
n4c=n4a.clone()
n4c.move(0,-5)
n4d=n4a.clone()
n4d.move(-5,0)
n4a.draw(win)
n4b.draw(win)
n4c.draw(win)
n4d.draw(win)

d5=d.clone()
d5.move(60,0)
n5a=n4a.clone()
n5a.move(15,0)
n5b=n4b.clone()
n5b.move(15,0)
n5c=n4c.clone()
n5c.move(15,0)
n5d=n4d.clone()
n5d.move(15,0)
n5e=n.clone()
n5e.move(60,0)
n5a.draw(win)
n5b.draw(win)
n5c.draw(win)
n5d.draw(win)
n5e.draw(win)

d1.draw(win)
d2.draw(win)
d3.draw(win)
d4.draw(win)
d5.draw(win)
