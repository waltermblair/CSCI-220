from graphics import *

win=GraphWin(320,240)
win.setCoords(0,0,100,100)

message=Text(Point(50,95),"Click to place the top left corner of your house")
message.draw(win)
p1=win.getMouse()
p1.draw(win)

message.setText("Click to place the bottom right corner of your house")
p2=win.getMouse()
p1.undraw()

dx1=p2.getX()-p1.getX()
dy1=p2.getY()-p1.getY()

p3=Point(p1.getX(),p1.getY()+dy1)
p4=Point(p1.getX()+dx1,p1.getY())

rect=Rectangle(p1,p2)
rect.draw(win)

message.setText("Click to place the top left corner of the front door")
p5=win.getMouse()
dx2=1/5*(p4.getX()-p1.getX())
dy2=p2.getY()-p5.getY()
p6=Point(p5.getX()+dx2,p5.getY()+dy2)

door=Rectangle(p5,p6)
door.draw(win)

message.setText("Click to place the center of the window")
p9=win.getMouse()

l=p6.getX()-p5.getX()
p10=p9.clone()
p10.move(-l/4,l/4)
p11=p9.clone()
p11.move(l/4,-l/4)

window=Rectangle(p10,p11)
window.draw(win)

message.setText("Click to place the height of your roof")
p12=win.getMouse()
p13=Point(p1.getX()+dx1/2,p12.getY())
roof=Polygon(p13,p1,p4)
roof.draw(win)

message.setText("Awww, cute!")
