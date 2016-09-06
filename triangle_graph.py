from graphics import *
print("This program draws a triangle from mouse clicks")
win=GraphWin()
win.setCoords(0.0,0.0,10.0,10.0)
xaxis=Line(Point(0.5,1),Point(9.5,1))
yaxis=Line(Point(0.5,1),Point(0.5,9.5))
message=Text(Point(5,0.25),"Click any three points in the graph")
xaxis.draw(win)
yaxis.draw(win)
message.draw(win)

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)
p3=win.getMouse()
p3.draw(win)

triangle=Polygon(p1,p2,p3)
triangle.setFill('pink')
triangle.draw(win)

message.setText("All done, click anywhere to quit.")
if win.getMouse():
    win.close()
